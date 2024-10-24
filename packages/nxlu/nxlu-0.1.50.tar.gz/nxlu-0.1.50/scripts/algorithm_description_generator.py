import argparse
import asyncio
import json
import logging
import os
import re
from pathlib import Path

import nest_asyncio
import networkx as nx
from community import community_louvain
from llama_index.core import Settings, get_response_synthesizer
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.schema import NodeWithScore, TextNode

from nxlu.config import NxluConfig
from nxlu.explanation.corpus import SUPPORTED_ALGORITHMS, normalize_name
from nxlu.explanation.rag import get_nodes_by_type
from nxlu.utils.control import init_llm_model

nest_asyncio.apply()

logger = logging.getLogger("nxlu")


class AlgorithmDocstringSummarizer:
    """Summarize algorithm docstrings using graph-based knowledge indexing."""

    def __init__(
        self,
        llm,
        neo4j_uri: str,
        neo4j_user: str,
        neo4j_password: str,
        neo4j_database: str,
        max_concurrent_tasks: int = 5,
    ):
        """
        Initialize the summarizer.

        Parameters
        ----------
        llm : object
            The language model to use for summarization.
        neo4j_uri : str
            The URI for the Neo4j database.
        neo4j_user : str
            The username for the Neo4j database.
        neo4j_password : str
            The password for the Neo4j database.
        neo4j_database : str
            The database name to connect to.
        max_concurrent_tasks : int, optional
            The maximum number of concurrent summarization tasks, by default 5.
        """
        self.llm = llm
        self.neo4j_uri = neo4j_uri
        self.neo4j_user = neo4j_user
        self.neo4j_password = neo4j_password
        self.neo4j_database = neo4j_database
        self.response_synthesizer = get_response_synthesizer(
            response_mode=ResponseMode.COMPACT
        )
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)

    @staticmethod
    def _clean_docstring(docstring: str) -> str:
        """
        Clean and normalize the docstring.

        Parameters
        ----------
        docstring : str
            The original docstring.

        Returns
        -------
        str
            The cleaned and normalized docstring.
        """
        docstring = docstring.split("References")[0]
        docstring = re.sub(r"-+\n", " ", docstring)
        docstring = re.sub(r"\[\d+\]_", "", docstring)
        docstring = re.sub(r"\s+", " ", docstring).strip()
        return docstring

    def _get_related_knowledge(self, algorithm_name: str) -> tuple[str, list]:
        """Retrieve related knowledge and nodes for an algorithm using a retriever.

        Parameters
        ----------
        algorithm_name : str
            The name of the algorithm.

        Returns
        -------
        tuple of str and list
            A tuple containing the related knowledge string and a list of NodeWithScore.
        """
        try:
            nodes_dicts = get_nodes_by_type(
                algorithm_type=algorithm_name.capitalize(),
                uri=self.neo4j_uri,
                user=self.neo4j_user,
                password=self.neo4j_password,
                database=self.neo4j_database,
            )
            if not nodes_dicts:
                logger.warning(f"No nodes retrieved for '{algorithm_name}'.")
                return "", []

            nodes = []
            for node_dict in nodes_dicts:
                content = node_dict["properties"].get("description", "")
                text_node = TextNode(text=content)
                node_with_score = NodeWithScore(node=text_node)
                nodes.append(node_with_score)

            related_knowledge = "\n".join([n.node.get_content() for n in nodes])

            logger.info(
                f"Retrieved context for '{algorithm_name}': {related_knowledge}"
            )
            logger.debug(f"Retrieved Nodes: {nodes}")

        except Exception:
            logger.exception(f"Failed to retrieve knowledge for '{algorithm_name}'")
            return "", []
        else:
            return related_knowledge, nodes

    async def summarize_algorithm(self, algorithm_name: str) -> dict:
        """
        Generate technical and colloquial summaries for an algorithm.

        Parameters
        ----------
        algorithm_name : str
            The name of the algorithm to summarize.

        Returns
        -------
        dict
            A dictionary containing 'technical' and 'colloquial' summaries.
        """
        async with self.semaphore:
            try:
                docstring = self._clean_docstring(
                    self._retrieve_docstring(algorithm_name)
                )
                related_knowledge, nodes = self._get_related_knowledge(
                    normalize_name(algorithm_name).capitalize()
                )
                if not nodes:
                    logger.warning(
                        f"No nodes retrieved for '{algorithm_name}'. Skipping summary."
                    )
                    return {"technical": "", "colloquial": ""}

                prompt_technical = (
                    f"You are an expert graph mathematician. Here is some relevant"
                    f" knowledge: {related_knowledge}\n\n"
                    f"Please summarize the following docstring in technical terms:\n"
                    f"{docstring}"
                )
                prompt_colloquial = (
                    f"You are a teacher and expert communicator. Here is some relevant "
                    f"knowledge: {related_knowledge}\n\n"
                    f"Please summarize the following docstring in colloquial terms "
                    f"(i.e. without any technical jargon):\n"
                    f"{docstring}"
                )

                technical_summary = await self.synthesize_summary(
                    prompt_technical, related_knowledge, nodes
                )
                colloquial_summary = await self.synthesize_summary(
                    prompt_colloquial, related_knowledge, nodes
                )
            except Exception:
                logger.exception(f"Failed to summarize '{algorithm_name}'")
                return {"technical": "", "colloquial": ""}
            else:
                return {
                    "technical": technical_summary,
                    "colloquial": colloquial_summary,
                }

    async def synthesize_summary(self, prompt: str, context: str, nodes: list) -> str:
        """
        Generate a summary using the ResponseSynthesizer.

        Parameters
        ----------
        prompt : str
            The prompt to send to the synthesizer.
        context : str
            The related knowledge context.
        nodes : list
            A list of NodeWithScore objects.

        Returns
        -------
        str
            The synthesized summary.
        """
        try:
            response = await asyncio.to_thread(
                self.response_synthesizer.synthesize,
                query=prompt,
                context=context,
                nodes=nodes,
            )
        except Exception:
            logger.exception("Failed to synthesize summary")
            return ""
        else:
            return response.response

    def _retrieve_docstring(self, algorithm_name: str) -> str:
        """
        Retrieve the docstring of a NetworkX algorithm.

        Parameters
        ----------
        algorithm_name : str
            The name of the algorithm.

        Returns
        -------
        str
            The docstring of the algorithm or an empty string if not found.
        """
        if algorithm_name in ["girvan_newman", "greedy_modularity_communities"]:
            alg_func = getattr(nx.algorithms.community, algorithm_name, None)
        elif algorithm_name == "best_partition":
            alg_func = getattr(community_louvain, algorithm_name, None)
        else:
            alg_func = getattr(nx, algorithm_name, None)

        if alg_func is None:
            logger.error(f"NetworkX has no attribute '{algorithm_name}'")
            return ""
        return alg_func.__doc__ or ""


def save_algorithm_docs_to_json(algorithm_docs: dict, filename: str):
    """
    Save algorithm_docs to a JSON file.

    Parameters
    ----------
    algorithm_docs : dict
        A dictionary containing algorithm documentation.
    filename : str
        The path to the JSON file where the documentation will be saved.

    Returns
    -------
    None
    """
    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with Path(filename).open(mode="w") as f:
            json.dump(algorithm_docs, f, indent=4)
        logger.info(f"algorithm_docs successfully saved to {filename}")
    except Exception:
        logger.exception(f"Failed to save algorithm_docs to {filename}")


def load_algorithm_docs_from_json(filename: str) -> dict:
    """
    Load algorithm_docs from a JSON file.

    Parameters
    ----------
    filename : str
        The path to the JSON file to load.

    Returns
    -------
    dict
        A dictionary containing the loaded algorithm documentation.
    """
    try:
        with Path(filename).open(mode="r") as f:
            algorithm_docs = json.load(f)
    except Exception:
        logger.exception(f"Failed to load algorithm_docs from {filename}")
        return {}
    else:
        return algorithm_docs


async def main(
    output: str,
):
    config = NxluConfig(
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
        model_name="gpt-4o-mini",
        temperature=0.2,
        llm_framework="llamaindex",
    )
    llm = init_llm_model(config)
    Settings.llm = llm

    summarizer = AlgorithmDocstringSummarizer(
        llm=llm,
        neo4j_uri=os.environ.get("NEO4J_URI", "neo4j://localhost:7687"),
        neo4j_user=os.environ.get("NEO4J_USERNAME", "neo4j"),
        neo4j_password=os.environ.get("NEO4J_PASSWORD", "neo4j"),
        neo4j_database="nxlu",
    )

    algorithm_summaries = await asyncio.gather(
        *[summarizer.summarize_algorithm(alg) for alg in SUPPORTED_ALGORITHMS]
    )

    algorithm_docs = dict(zip(SUPPORTED_ALGORITHMS, algorithm_summaries))

    save_algorithm_docs_to_json(algorithm_docs, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="NxLU -- Algorithm Description Generator"
    )
    parser.add_argument(
        "--output",
        default="nxlu/data/algorithm_docs.json",
        help="Output JSON file for algorithm docs",
    )
    args = parser.parse_args()

    asyncio.run(
        main(
            args.output,
        )
    )
