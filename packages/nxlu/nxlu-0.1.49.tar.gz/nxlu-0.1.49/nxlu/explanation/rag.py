import json
import logging
import os
import re

import nest_asyncio
import numpy as np
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.graphs import Neo4jGraph
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from nxlu.explanation.corpus import load_corpus, load_docs_from_jsonl

nest_asyncio.apply()

logger = logging.getLogger("nxlu")

__all__ = ["Neo4jHelper", "GraphRAGPipeline", "get_nodes_by_type"]


class Neo4jHelper:
    def __init__(self, uri, user, password, database):
        """Initialize the Neo4jHelper.

        Parameters
        ----------
        uri : str
            The URI for the Neo4j database.
        user : str
            The username for the Neo4j database.
        password : str
            The password for the Neo4j database.
        database : str
            The database name to connect to.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self):
        """Close the Neo4j database connection."""
        self.driver.close()

    def add_relationship(self, source_node, target_node, relationship):
        """Add a relationship between two nodes in the Neo4j database.

        Parameters
        ----------
        source_node : Node
            The source node.
        target_node : Node
            The target node.
        relationship : dict
            A dictionary containing the relationship type and description.
        """
        with self.driver.session(database=self.database) as session:
            session.write_transaction(
                self._create_relationship, source_node, target_node, relationship
            )

    @staticmethod
    def _create_relationship(tx, source_node, target_node, relationship):
        """Create a relationship between two nodes in a transaction.

        Parameters
        ----------
        tx : Transaction
            The Neo4j transaction object.
        source_node : Node
            The source node.
        target_node : Node
            The target node.
        relationship : dict
            A dictionary containing the relationship type and description.
        """
        relationship_type = relationship["relation"].replace(" ", "_")
        query = (
            "MATCH (a:Node {name: $source_name}) "
            "MATCH (b:Node {name: $target_name}) "
            f"MERGE (a)-[r:{relationship_type}]->(b) "
            "SET r.description = $description"
        )
        tx.run(
            query,
            source_name=source_node.properties.get("name", ""),
            target_name=target_node.properties.get("name", ""),
            description=relationship.get("description", ""),
        )

    def delete_nodes_in_list(self, node_names):
        """Delete nodes from the Neo4j database that are in the provided list.

        Parameters
        ----------
        node_names : list of str
            List of node names to delete.
        """
        query = """
        MATCH (n)
        WHERE toLower(n.name) IN $names
        DETACH DELETE n
        """
        node_names = [name.lower() for name in node_names]

        with self.driver.session(database=self.database) as session:
            result = session.run(query, names=node_names)
            deleted_count = result.consume().counters.nodes_deleted
            logger.info(f"Deleted {deleted_count} nodes present in the provided list.")

    def delete_null_nodes(self):
        """Delete nodes from the Neo4j database where the 'name' property is NULL."""
        query = """
        MATCH (n)
        WHERE n.name IS NULL OR n.name = ''
        DETACH DELETE n
        """
        with self.driver.session(database=self.database) as session:
            result = session.run(query)
            deleted_count = result.consume().counters.nodes_deleted
            logger.info(
                f"Deleted {deleted_count} nodes with empty or null 'name' properties."
            )


class GraphRAGPipeline:
    def __init__(
        self,
        documents_path,
        corpus_path,
        allowed_nodes,
        relationship_prompt,
        extraction_prompt,
        system_prompt,
        corpus_embedding_model="witiko/mathberta",
        rag_model="gpt-4o-2024-08-06",
        neo4j_db="nxlu",
    ):
        """Initialize the GraphRAGPipeline.

        Parameters
        ----------
        documents_path : str
            Path to the documents in JSONL format.
        corpus_path : str
            Path to the graph theory corpus text file.
        """
        self.documents_path = documents_path
        self.corpus_path = corpus_path
        self.corpus_embedding_model = corpus_embedding_model
        self.rag_model = rag_model
        self.neo4j_db = neo4j_db
        self.allowed_nodes = allowed_nodes
        self.relationship_prompt = relationship_prompt
        self.extraction_prompt = extraction_prompt
        self.system_prompt = system_prompt
        self.documents = []
        self.combined_texts = []
        self.graph_documents = []
        self.all_nodes = []
        self.filtered_nodes = []
        self.bad_node_names = []
        self.corpus_embeddings = None
        self.model = None
        self.prompt = None
        self.kg_transformer = None
        self.graph = None
        self.neo4j_helper = None
        self.embedding_model = None
        self.corpus = []

    def load_documents(self):
        """Load documents from a JSONL file."""
        self.documents = load_docs_from_jsonl(self.documents_path)

    def split_and_combine_texts(self):
        """Split and combine texts into chunks suitable for processing."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000,
            chunk_overlap=750,
            separators=["\n\n", "\n", " ", ""],
        )
        combined_texts = []
        current_text = ""
        max_length = 10000

        chunks = text_splitter.split_documents(self.documents)
        for doc in chunks:
            if len(current_text) + len(doc.page_content) + 1 < max_length:
                current_text += " " + doc.page_content
            else:
                combined_texts.append(Document(page_content=current_text.strip()))
                current_text = doc.page_content

        if current_text:
            combined_texts.append(Document(page_content=current_text.strip()))

        self.combined_texts = combined_texts

    def prepare_prompt_and_model(self):
        """Prepare the prompt template and initialize the language model."""
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    self.system_prompt,
                ),
                ("user", self.extraction_prompt),
            ]
        )

        self.model = ChatOpenAI(temperature=0.1, model_name=self.rag_model)

    def process_documents(self):
        """Process documents to extract graph information and store in Neo4j."""
        self.kg_transformer = LLMGraphTransformer(
            llm=self.model,
            prompt=self.prompt,
            allowed_nodes=self.allowed_nodes,
            node_properties=["name", "type", "description"],
            relationship_properties=["source", "target", "relation", "description"],
            strict_mode=True,
        )

        self.graph = Neo4jGraph(
            url=os.environ.get("NEO4J_URI", "neo4j"),
            username=os.environ.get("NEO4J_USERNAME", "neo4j"),
            password=os.environ.get("NEO4J_PASSWORD", "neo4j"),
            database=self.neo4j_db,
        )

        self.graph_documents = self.kg_transformer.convert_to_graph_documents(
            self.combined_texts
        )

        self.graph.add_graph_documents(
            self.graph_documents, include_source=True, baseEntityLabel=True
        )

    def filter_nodes(self):
        """Filter nodes based on predefined criteria."""
        self.all_nodes = []
        for graph_doc in self.graph_documents:
            self.all_nodes.extend(list(graph_doc.nodes))

        self.filtered_nodes = []
        for graph_doc in self.graph_documents:
            self.filtered_nodes.extend(
                [
                    node
                    for node in graph_doc.nodes
                    if node.type.lower() in self.allowed_nodes
                    and node.properties != {}
                    and node.properties.get("name")
                    and node.properties.get("description")
                    and not len(str(node.properties.get("description"))) < 20
                    and node.id
                ]
            )
        self.bad_node_names = [
            node.properties.get("name", "").strip()
            for node in self.all_nodes
            if node not in self.filtered_nodes
        ]

    def load_corpus(self):
        """Load the corpus from a text file."""
        self.corpus = load_corpus(self.corpus_path)

    def encode_corpus(self):
        """Encode the corpus using a SentenceTransformer."""
        self.embedding_model = SentenceTransformer(self.corpus_embedding_model)
        self.corpus_embeddings = self.embedding_model.encode(
            self.corpus, convert_to_tensor=False
        )

    def delete_bad_nodes(self):
        """Delete nodes that do not meet the criteria from the Neo4j database."""
        self.neo4j_helper = Neo4jHelper(
            uri=os.environ.get("NEO4J_URI", "neo4j://localhost:7687"),
            user=os.environ.get("NEO4J_USERNAME", "neo4j"),
            password=os.environ.get("NEO4J_PASSWORD", "neo4j"),
            database=self.neo4j_db,
        )
        self.neo4j_helper.delete_nodes_in_list(self.bad_node_names)

    def is_corpus_related(self, text: str, corpus: list) -> bool:
        """Determine if a given text is related to graph theory.

        Parameters
        ----------
        text : str
            The text to evaluate.
        corpus : list
            List of keywords related to graph theory.

        Returns
        -------
        bool
            True if related to graph theory, False otherwise.
        """
        if not text:
            return False
        text = text.lower()
        return any(keyword.lower() in text for keyword in corpus)

    def prune_node(self, node) -> bool:
        """Check if a node is related to graph theory.

        Parameters
        ----------
        node : Node
            The node to check.

        Returns
        -------
        bool
            True if the node is related, False otherwise.
        """
        name = node.properties.get("name", "")
        description = node.properties.get("description", "")
        return self.is_corpus_related(
            name, self.allowed_nodes
        ) or self.is_corpus_related(description, self.allowed_nodes)

    def prune_relationship(self, relation) -> bool:
        """Check if a relationship is relevant to graph theory.

        Parameters
        ----------
        relation : dict
            The relationship to check.

        Returns
        -------
        bool
            True if the relationship is relevant, False otherwise.
        """
        description = relation.get("description", "")
        related = self.is_corpus_related(description, self.allowed_nodes)
        if related:
            logger.debug(f"Relationship '{description}' is related to graph theory.")
        else:
            logger.debug(
                f"Relationship '{description}' is NOT related to graph theory."
            )
        return related

    def get_embedding(self, text):
        """Generate embeddings for the given text.

        Parameters
        ----------
        text : str
            The text to encode.

        Returns
        -------
        np.ndarray
            The embedding vector.
        """
        return self.embedding_model.encode(text, convert_to_tensor=False)

    def filter_nodes_by_similarity(self, nodes, corpus_embeddings, threshold=0.95):
        """Filter nodes by calculating cosine similarity with the corpus embeddings.

        Parameters
        ----------
        nodes : list
            List of Node objects.
        corpus_embeddings : np.ndarray
            Precomputed embeddings for the graph theory corpus.
        threshold : float, optional
            Similarity threshold for retaining nodes.

        Returns
        -------
        list
            List of filtered nodes.
        """
        filtered_nodes = []
        for node in nodes:
            node_name = node.properties.get("name", "")
            node_description = node.properties.get("description", "")
            node_type = node.properties.get("type", "")
            if not node_name or not node_description or not node_type:
                continue
            node_embedding = self.get_embedding(
                f"{node_name} {node_type} {node_description}"
            )
            similarity_scores = cosine_similarity([node_embedding], corpus_embeddings)
            max_similarity = np.max(similarity_scores)
            if max_similarity > threshold:
                filtered_nodes.append(node)
        return filtered_nodes

    def determine_relationship(self, node_a, node_b) -> dict | None:
        """Determine the relationship between two nodes.

        Parameters
        ----------
        node_a : Node
            The first node.
        node_b : Node
            The second node.

        Returns
        -------
        dict or None
            The relationship dictionary or None if not applicable.
        """
        formatted_prompt = self.relationship_prompt.format(
            node_a_name=node_a.properties.get("name", ""),
            node_a_type=node_a.properties.get("type", ""),
            node_a_description=node_a.properties.get("description", ""),
            node_b_name=node_b.properties.get("name", ""),
            node_b_type=node_b.properties.get("type", ""),
            node_b_description=node_b.properties.get("description", ""),
        )

        try:
            response = self.model(formatted_prompt)

            if hasattr(response, "content"):
                content = response.content
            elif hasattr(response, "text"):
                content = response.text
            elif hasattr(response, "generations") and len(response.generations) > 0:
                content = response.generations[0].message.content
            else:
                logger.error("Unexpected response structure from the model.")

            logger.debug(f"Raw model response: {content}")

            content = re.sub(r"^```json\s*", "", content)
            content = re.sub(r"\s*```$", "", content)
            content = content.strip()

            logger.debug(f"Cleaned model response: {content}")

            if not (content.startswith("{") and content.endswith("}")):
                logger.error(
                    f"Response does not start with '{{' or end with '}}': {content}"
                )

            relationship = json.loads(content)

            if "relation" in relationship and "description" in relationship:
                logger.debug(f"Valid relationship determined: {relationship}")
                return relationship
            logger.warning(f"Invalid relationship format received: {relationship}")

        except json.JSONDecodeError:
            logger.exception("Failed to parse relationship JSON")
            logger.exception(f"Content received: {content}")
            return None
        except Exception:
            logger.exception("An error occurred while determining relationship")
            return None
        else:
            return None

    def link_and_prune_nodes(self, similarity_threshold=0.98):
        """Link and prune nodes and relationships across documents."""
        logger.info(f"Starting to link and prune {len(self.filtered_nodes)} nodes.")
        total_relationships_added = 0

        filtered_nodes = self.filter_nodes_by_similarity(
            self.filtered_nodes, self.corpus_embeddings, threshold=similarity_threshold
        )
        logger.info(f"Filtered {len(self.filtered_nodes) - len(filtered_nodes)} nodes.")

        for i, node_a in enumerate(filtered_nodes):
            if not self.prune_node(node_a):
                logger.debug(
                    f"Skipping node '{node_a.properties.get('name', '')}' as it's not "
                    f"related to the corpus."
                )
                continue

            for j, node_b in enumerate(filtered_nodes):
                if i >= j:
                    continue
                if not self.prune_node(node_b):
                    logger.debug(
                        f"Skipping node '{node_b.properties.get('name', '')}' as it's "
                        f"not related to the corpus."
                    )
                    continue

                relationship = self.determine_relationship(node_a, node_b)

                if relationship and self.prune_relationship(relationship):
                    try:
                        self.neo4j_helper.add_relationship(node_a, node_b, relationship)
                        logger.info(
                            f"Added relationship between "
                            f"'{node_a.properties.get('name', '')}' and "
                            f"'{node_b.properties.get('name', '')}'."
                        )
                        total_relationships_added += 1
                    except Exception:
                        logger.exception(
                            f"Failed to add relationship between "
                            f"'{node_a.properties.get('name', '')}' and "
                            f"'{node_b.properties.get('name', '')}'"
                        )

        logger.info(
            f"Finished linking and pruning nodes. Total relationships added: "
            f"{total_relationships_added}."
        )
        self.neo4j_helper.close()

    def run(self):
        """Execute the full analysis pipeline."""
        self.load_documents()
        self.split_and_combine_texts()
        self.prepare_prompt_and_model()
        self.process_documents()
        self.filter_nodes()
        self.load_corpus()
        self.encode_corpus()
        self.delete_bad_nodes()
        try:
            self.link_and_prune_nodes()
        except Exception:
            logger.exception("An error occurred while linking and pruning nodes")


def get_nodes_by_type(
    algorithm_type: str, uri: str, user: str, password: str, database: str
) -> list:
    """
    Retrieve nodes from Neo4j based on the algorithm type.

    Parameters
    ----------
    algorithm_type : str
        The type of the algorithm (node.type).
    uri : str
        The Bolt URI for Neo4j connection.
    user : str
        Neo4j username.
    password : str
        Neo4j password.
    database : str
        The Neo4j database name.

    Returns
    -------
    list
        A list of dictionaries containing node details.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    nodes = []
    try:
        with driver.session(database=database) as session:
            cypher_query = """
            CALL apoc.cypher.run(
                'MATCH (n) WHERE $label IN labels(n) RETURN n',
                {label: $algorithm_type}
            ) YIELD value
            RETURN value.n AS n
            """
            result = session.run(cypher_query, algorithm_type=algorithm_type)

            for record in result:
                node = record["n"]
                nodes.append(
                    {
                        "id": node.id,
                        "labels": list(node.labels),
                        "properties": dict(node),
                    }
                )
    except Exception:
        logger.exception(f"Failed to retrieve nodes for label '{algorithm_type}'")
    finally:
        driver.close()
    return nodes
