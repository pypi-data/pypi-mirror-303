import asyncio
import logging
import warnings

import networkx as nx

from nxlu.config import Intent, NxluConfig
from nxlu.explanation.classify import IntentClassifier
from nxlu.io import load_algorithm_docs, load_algorithm_encyclopedia
from nxlu.processing.analyze import GraphProperties, analyze_relationships
from nxlu.processing.embed import QuerySubgraph
from nxlu.processing.optimize import (
    AlgorithmNominator,
    GraphAlgorithmElector,
    GraphPreprocessingSelector,
)
from nxlu.processing.preprocess import CleanGraph
from nxlu.processing.summarize import characterize_graph, format_algorithm_results
from nxlu.utils.control import ResourceManager
from nxlu.utils.misc import scrub_braces

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")

__all__ = ["GraphInterrogator"]


class GraphInterrogator:
    """A class to interrogate and analyze NetworkX graphs using integrated algorithms
    and language models.

    Attributes
    ----------
    config : NxluConfig
        Configuration settings for the model.
    llm : Any
        Initialized language model.
    classifier : Any
        Zero-shot classification pipeline.
    algorithm_applicability : Dict[str, Dict[str, Any]]
        Dictionary mapping algorithms to their applicability conditions.
    algorithm_classifier : GraphAlgorithmElector
        Classifier to handle algorithm selection.
    applicable_algorithms : List[str]
        List of algorithms applicable to the graph.
    preprocessing_config : Any
        Configuration for graph preprocessing.
    graph_summary : str
        Summary of the graph.
    selected_algorithms : List[str]
        Algorithms selected based on classification.
    results : Dict[str, Any]
        Results from applied algorithms.
    """

    def __init__(self, config: NxluConfig):
        """Initialize the GraphInterrogator with necessary models and classifiers.

        Parameters
        ----------
        config : NxluConfig
            Configuration settings for the model.
        backend : BaseBackend
            The backend instance to use for running algorithms.
        """
        self.config = config
        self.algorithm_applicability = load_algorithm_encyclopedia()
        self.intent_classifier = IntentClassifier()
        if self.config.enable_subgraph_retrieval:
            self.query_subgraph_slicer = QuerySubgraph(
                embedding_model_name=self.config.embedding_model_name
            )
        self.nominator = AlgorithmNominator(
            applicability_dict=self.algorithm_applicability,
            resource_manager=ResourceManager(),
            include_algorithms=self.config.include_algorithms,
            exclude_algorithms=self.config.exclude_algorithms,
            enable_classification=self.config.enable_classification,
            enable_resource_constraints=self.config.enable_resource_constraints,
        )
        self.algorithm_classifier = GraphAlgorithmElector(
            algorithm_docs=load_algorithm_docs(),
            applicability_dict=self.algorithm_applicability,
            include_algorithms=self.config.include_algorithms,
            exclude_algorithms=self.config.exclude_algorithms,
            enable_classification=self.config.enable_classification,
        )

    async def reason_async(
        self,
        graph: nx.Graph,
        query: str,
        intent: list[Intent] | None = None,
    ) -> str:
        """Asynchronously generate reasoning based on the graph and query.

        Parameters
        ----------
        graph : nx.Graph
            The NetworkX graph to analyze.
        query : str
            The user's query.
        intent : List[Intent]
            Inferred high-level intents from user queries. Default is exploration.

        Returns
        -------
        str
            The reasoning result.
        """
        if intent is None:
            intent = [Intent.EXPLORATION]
        loop = asyncio.get_event_loop()
        graph_info = await loop.run_in_executor(None, self.reason, graph, query, intent)
        return graph_info

    def reason(
        self,
        graph: nx.Graph,
        query: str,
        intent: list[Intent] | None = None,
    ) -> dict | str:
        """Generate reasoning based on the graph and query.

        Parameters
        ----------
        graph : nx.Graph
            The NetworkX graph to analyze. If None, generate a simple response.
        query : str
            The user's query.
        intent : List[Intent]
            Inferred high-level intents from user queries. Default is exploration.

        Returns
        -------
        str
            The reasoning result.
        """
        if intent is None:
            intent = [Intent.EXPLORATION]

        if self.config.enable_subgraph_retrieval:
            try:
                subgraph = self.query_subgraph_slicer.create_query_subgraph(
                    graph, query
                )
            finally:
                self.query_subgraph_slicer.cleanup()
        else:
            subgraph = graph

        graph_props = GraphProperties(subgraph)
        applicable_algorithms = self.nominator.select_algorithms(graph_props, query)

        if not applicable_algorithms:
            return "No applicable algorithms found for the given graph."

        preprocessing_classifier = GraphPreprocessingSelector(
            self.algorithm_applicability
        )
        preprocessing_config = preprocessing_classifier.select_preprocessing_steps(
            subgraph, applicable_algorithms
        )

        cleaner = CleanGraph(subgraph, preprocessing_config)
        clean_subgraph = cleaner.clean()

        try:
            clean_props = GraphProperties(clean_subgraph)
            graph_summary, relevant_authorities, relevant_hubs = characterize_graph(
                graph=clean_subgraph,
                graph_props=clean_props,
                user_query=query,
                detect_domain=True,
                embedding_model_name=self.config.embedding_model_name,
            )
        except Exception:
            logger.exception("Error characterizing graph. Using minimal summary.")
            graph_summary = f"Graph with {clean_subgraph.number_of_nodes()} nodes and "
            f"{clean_subgraph.number_of_edges()} edges."
            relevant_authorities, relevant_hubs = [], []
        important_nodes = list(set(relevant_authorities) | set(relevant_hubs))

        elected_algorithms = self.algorithm_classifier.elect_algorithms(
            query=query,
            graph_summary=graph_summary,
            user_intent=intent,
            candidates=applicable_algorithms,
        )

        if not elected_algorithms:
            return "No relevant algorithms matched the query and graph properties."

        results = self.algorithm_classifier.apply_elected_algorithms(
            graph=clean_subgraph,
            algorithms=elected_algorithms,
            query=query,
        )

        consolidated_results = list(results.items())
        formatted_results = format_algorithm_results(consolidated_results)
        if len(important_nodes) > 0:
            subgraph_relationships = analyze_relationships(
                nx.induced_subgraph(subgraph, important_nodes)
            )
        else:
            subgraph_relationships = "No hubs or authorities identified"

        compiled_results = {
            "Graph Summary": graph_summary,
            "Descriptions of Applied Algorithms": dict(
                zip(
                    elected_algorithms,
                    [
                        self.algorithm_classifier.algorithm_docs[alg]
                        for alg in elected_algorithms
                    ],
                )
            ),
            "Graph Analysis": formatted_results,
            "Relationships Among Hubs and Authorities": subgraph_relationships,
        }

        return scrub_braces(compiled_results)
