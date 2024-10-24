from collections.abc import Callable

ALGORITHM_SUBMODULES = [
    "networkx.linalg.algebraicconnectivity",
    "networkx.algorithms.centrality",
    "networkx.algorithms.centrality.load",
    "networkx.algorithms.clique",
    "networkx.algorithms.cluster",
    "networkx.algorithms.components",
    "networkx.algorithms.connectivity",
    "networkx.algorithms.efficiency_measures",
    "networkx.algorithms.cycles",
    "networkx.algorithms.flow",
    "networkx.algorithms.shortest_paths",
    "networkx.algorithms.assortativity",
    "networkx.algorithms.lowest_common_ancestors",
    "networkx.algorithms.wiener",
    "networkx.algorithms.community",
    "networkx.algorithms.coloring",
    "networkx.algorithms.isomorphism",
    "networkx.algorithms.triads",
    "networkx.algorithms.bridges",
    "networkx.algorithms.richclub",
    "networkx.algorithms.matching",
    "networkx.algorithms.dag",
    "networkx.algorithms.tree",
    "networkx.algorithms.approximation",
    "networkx.algorithms.link_analysis",
    "networkx.algorithms.traversal",
    "networkx.algorithms.approximation",
    "networkx.algorithms.link_prediction",
    "networkx.algorithms.vitality",
    "networkx.algorithms.core",
    "networkx.algorithms.distance_measures",
]

CUSTOM_ALGORITHMS: dict[str, Callable] = {}

# used to determine if an algorithm's output should be
# handled as a dictionary.
GENERATORS_TO_DICT = {
    "all_pairs_shortest_path",
    "all_pairs_dijkstra_path",
    "all_pairs_bellman_ford_path",
    "all_pairs_shortest_path_length",
    "all_pairs_dijkstra_path_length",
    "all_pairs_bellman_ford_path_length",
    "bellman_ford_path",
    "shortest_path_length",
    "dijkstra_path_length",
    "bellman_ford_path_length",
    "shortest_path",
    "dijkstra_path",
}

REQUIRES_SOURCE_TARGET = {
    "shortest_path",
    "dijkstra_path",
    "bellman_ford_path",
    "shortest_simple_paths",
    "single_source_shortest_path",
    "single_source_dijkstra_path",
    "single_source_bellman_ford_path",
}

ALGORITHM_TYPES = [i.split(".")[-1] for i in ALGORITHM_SUBMODULES]


SYSTEM_PROMPT = """
You are an expert in graph theory and data analysis. Analyze the provided
graph information and user queries to generate clear, insightful, and
sufficiently detailed explanations. Focus on interpreting the results of
the applied algorithms, uncovering hidden patterns, unexpected
relationships, or counterintuitive findings. Mention potential
alternative interpretations or areas requiring further investigation if
applicable. Avoid stating the obvious or sharing superfluous insights. Please avoid
detailed technical descriptions unless they help to shed light on your chain-of-thought.
"""

GENERAL_EXPLORATION_PROMPT = """
Analyze the given graph G with the following objectives:
1. Identify key global and local topological properties.
2. Detect important nodes or communities using relevant centrality measures.
3. Uncover any notable patterns or anomalies in the graph structure.
4. Suggest potential domain-specific insights based on the graph's attributes, if they
are available.

Provide a concise summary of your findings, highlighting the most salient aspects of
the graph's topology and potential implications for its underlying domain.
"""

PATH_ANALYSIS_PROMPT = """
Examine the paths among nodes in graph G, focusing on:
1. Shortest paths between key nodes (if specified, otherwise sample representative
paths).
2. Distribution of path lengths across the graph.
3. Identification of any bottlenecks or critical nodes in common paths.
4. Potential implications of path structures for information flow or network resilience.

Summarize your findings, emphasizing how the path characteristics might impact the
network's functionality or efficiency.
"""

TEMPORAL_ANALYSIS_PROMPT = """
For the time-evolving graph G, investigate:
1. Changes in key graph metrics over time (e.g., number of nodes/edges, density,
diameter).
2. Evolution of community structures or important nodes.
3. Emergence or dissolution of significant patterns or subgraphs.
4. Potential factors driving the observed temporal changes.

Summarize the most significant temporal trends and their potential implications for the
network's dynamics.
"""

CENTRALITY_ANALYSIS_PROMPT = """
Conduct a comprehensive centrality analysis on graph G:
1. Calculate and compare multiple centrality measures (e.g., degree, betweenness,
eigenvector).
2. Identify and characterize the most central nodes according to each measure.
3. Analyze the distribution of centrality scores across the network.
4. Interpret the centrality results in the context of the graph's domain.

Provide insights into the role and importance of central nodes, and how different
centrality measures reveal various aspects of the network's structure.
"""

ANOMALY_DETECTION_PROMPT = """
Investigate graph G for potential anomalies or unusual structures:
1. Identify nodes or edges with exceptional properties (e.g., unusually high degree,
betweenness).
2. Detect subgraphs with unexpected density or connectivity patterns.
3. Find nodes or edges that deviate significantly from the overall graph structure.
4. Assess the potential significance of these anomalies in the context of the graph's
domain.

Summarize your findings, highlighting the most notable anomalies and their possible
implications for the network's function or integrity.
"""

GRAPHRAG_ALGORITHM_RELATION_PROMPT = """
Given the following two graph algorithms:

**Algorithm 1:**
- **Name:** {node_a_name}
- **Type:** {node_a_type}
- **Description:** {node_a_description}

**Algorithm 2:**
- **Name:** {node_b_name}
- **Type:** {node_b_type}
- **Description:** {node_b_description}

**Task:** Determine if there is a meaningful, graph theoretical relationship
between these two algorithms. If so, specify the type of relationship and
provide a brief description.

**Output Format:**
{{
    "relation": "RelationshipType",
    "description": "Brief description of the relationship."
}}
"""

GRAPHRAG_ALGORITHM_DOCUMENT_EXTRACTION_PROMPT = """
Analyze the following text to extract information relevant to graph theory or
network science, focusing on definitions, use-cases, and interrelationships of
graph algorithms.

**Tasks:**
1. **Identify Algorithms (entities):**
    - Extract graph algorithms explicitly mentioned in the text.
    - For each identified algorithm, provide:
        - **Name**: The exact name of the algorithm.
        - **Type**: The category or type of the algorithm.
            - Permissible values are:
                ['assortativity', 'bridges', 'centrality', 'clique', 'cluster',
                'coloring', 'community', 'components', 'connectivity', 'core',
                'cycles', 'distance', 'efficiency', 'flow', 'link prediction',
                'lowest common ancestors', 'path', 'richclub', 'tree', 'triads',
                'vitality']
        - **Description**: A meaningful description, of at least 25 characters,
        based on the immediate context in the text and relevant to graph theory
        or network science only.

2. **Determine Relationships (relations):**
    - Extract meaningful relationships between the identified algorithms based
    on their respective contexts in the text.
    - For each relationship, specify:
        - **Source**: The name of the first identified algorithm.
        - **Target**: The name of the second identified algorithm.
        - **Relation**: The type of relationship.
        - **Description**: How the two identified algorithms relate **within the
        context** of the text in which they appear.

**Output Format:**
- Provide the extracted information in **valid JSON** format as shown below.
- **Do not include any additional text**, explanations, or markdown. The
response should be **pure JSON**.

**Example:**

*Given the text:*
"We applied k-core decomposition and used the PageRank algorithm to rank nodes
by importance in the identified dense subgraphs."

*The extracted entities and relations should be:*
```json
{{
    "entities": [
        {{"name": "k-core", "type": "Centrality", "description": "Algorithm to
        identify dense subgraphs."}},
        {{"name": "PageRank", "type": "Centrality", "description": "Algorithm
        used to rank nodes by importance in a network."}}
    ],
    "relations": [
        {{"source": "k-core", "target": "PageRank", "relation": "Dependency",
        "description": "PageRank ranks nodes within the dense subgraphs
        identified by k-core."}}
    ]
}}
```

**Please respond strictly in the above JSON format without any additional text
or explanations:**

"""

GRAPHRAG_ALGORITHM_SYSTEM_PROMPT = (
    "You are a mathematician with specialization in graph theory."
)


class AnalysisPrompts:
    GENERAL_EXPLORATION = GENERAL_EXPLORATION_PROMPT
    PATH_ANALYSIS = PATH_ANALYSIS_PROMPT
    TEMPORAL_ANALYSIS = TEMPORAL_ANALYSIS_PROMPT
    CENTRALITY_ANALYSIS = CENTRALITY_ANALYSIS_PROMPT
    ANOMALY_DETECTION = ANOMALY_DETECTION_PROMPT

    @staticmethod
    def get_prompt(analysis_type: str) -> str:
        return getattr(
            AnalysisPrompts, analysis_type.upper(), AnalysisPrompts.GENERAL_EXPLORATION
        )


PUBLISHERS = [
    "John Wiley & Sons",
    "McGraw-Hill Book Company",
    "Academic Press",
    "Elsevier",
    "Pergamon Press",
    r"M\.I\.T\. Press",
    "Interscience Division",
    "John Wiley & Sons, Inc.",
    "McGraw-Hill Book Company, Inc.",
    "Academic Press, Inc.",
]


NOISE_PATTERNS = [
    r"www\.\S+",  # Matches URLs
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  # Matches emails
    r"\d{3}-\d{3}-\d{4}",  # Matches phone numbers (e.g., 123-456-7890)
    r"\d{1,2}:\d{2}(?:[:]\d{2})?\s*(?:AM|PM|am|pm)?",  # Matches timestamps (e.g., "12:30 PM" or "18:45")
    r"\[\d+-\d+\]",  # Matches references like "[1-12]"
    r"Fig\.\s*\d+",  # Matches figure references like "Fig. 1"
    r"\b[A-Z]{2,}(?:\s+[A-Z]{2,}){0,2}\b",  # Matches words/phrases written in all caps
    r"(\d+\.){1,2}",  # Matches numbered section headings like "1.2."
    r"etc\.\)",  # Matches "etc.)"
    r"\b(?:Table|Figure|Appendix)\s*\d+",  # Matches table/figure references like "Table 5", "Figure 2"
    r"Copyright\s?\d{4}",  # Matches copyright text like "Copyright 2023"
    r"(ISBN|ISSN)\s?:?\s?\d+",  # Matches ISBN or ISSN numbers
    r"\bDOI:\s?\S+",  # Matches DOI references
    r"@\w+",  # Matches Twitter handles or mentions
    r"#\w+",  # Matches hashtags
    r"\d{1,2}/\d{1,2}/\d{2,4}",  # Matches dates like "12/31/2023" or "31/12/23"
    r"\d{4}-\d{4}",  # Matches year ranges like "2020-2023"
    r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}",  # Matches full dates like "March 12, 2023"
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4},\d+-\d+\b",
    r"\bIssue\s*\d+",  # Matches issue numbers like "Issue 5"
    r"\b(?:Vol\.|Volume)\s*\d+",  # Matches volume references like "Vol. 3"
    r"No\.\s*\d+",  # Matches "No. 3" for journal or publication numbering
    r"Accessed\s?\d{1,2}\s\w+\s\d{4}",  # Matches "Accessed 5 July 2023"
    r"\s+\b[IVXLCDM]+\b\s+",  # Matches Roman numerals in standalone form (e.g., "IV" or "XX")
    r"(http|https):\/\/\S+",  # Matches full URLs (alternative to 'www')
    r"^\s*\[\s*\w+.*?\s*\]\s*$",  # Matches standalone references (e.g., "[Smith et al., 2019]")
    r"^\s*(?:Chapter|Section)\s*\d+",  # Matches "Chapter 3" or "Section 2" headings
    # r"^\s*\*\s*$",  # Matches bullet points (e.g., "*")
    r"^\s*(?:NOTE|IMPORTANT|WARNING|CAUTION|DISCLAIMER):.*$",  # Matches cautionary or note phrases
    r"^\s*References.*$",  # Matches "References" heading commonly found in academic texts
    r"\(see\s.*?\)",  # Matches parenthetical references like "(see Fig. 1)"
    r"\s{2,}",  # Matches excessive spaces (more than two consecutive spaces)
    r"\bversion\s+\S+\s+\d{1,2},?\s+\d{4}\b",  # Matches version dates like "version September 14, 2024"
    r"\bpage\s+\d+\b",  # Matches page references like "page 399",
    r"(?i)(?:[A-Z]\.\s*){1,4},\s*[^,]+,\s*(?:John Wiley & Sons|McGraw-Hill|Pergamon|Academic|Elsevier).*?,\s*\w+,\s*\d{4},?",
    r"\b[A-Z]\.\s[A-Z][a-zA-Z]+,\s.*?,\s*(?:J\.|Journal of).*?,\s*\d{4},\s*\d+",  # Example for journal articles
    r"^'?[A-Z]\.\s*[A-Z]\.\s*,\s*(?:and\s*)?(?:[A-Z]\.\s*)?,.*",  # multiple initials with commas
    r",\s*\d{4},\s*\d+",  # Matches ", 1968, 187"
    r",\s*\d{4}\s*,\s*\d+",  # Matches ", 1965, 43"
    # r"\b[A-Z]\.\s[A-Z][a-zA-Z]+,\s",  # Matches patterns like "W. Feller, ",
    r",\s*(?:John Wiley & Sons|McGraw-Hill Book Company|Pergamon Press|Academic Press|Elsevier Publishing Company),\s*\w+,\s*\d{4}",  # Adjust publisher names as needed,
    r"This article is protected by copyright\..*?All rights reserved\..*?",
    r"Downloaded from [\w\s]*?(?:Wiley|Elsevier|Springer|JSTOR|PubMed|IEEE).*?(?:Terms and Conditions|for rules of use).*?",
    r"Terms and Conditions.*?rules of use.*?(?:on Wiley|on Springer|on Elsevier|on PubMed|on JSTOR)?",  # General terms and conditions
    r"Endnotes.*",
    r"Affiliation.*",
    r"Corresponding\s*author.*",
    r"Footnotes.*",
    r"Publication\s*date.*",
    r",\s*,\s*,",  # Matches ", , ,"
    r"\[\d+\]",  # Match [7]
    r"\[\d+(?:-\d+)?\]",  # Match [7] and [1-5]
    r"\[\d+(?:,\s?\d+)*\]",  # Match [1,2,3] style references
    r"Affiliation.*",  # Capture affiliation metadata
    r"Corresponding\s*author.*",  # Match correspondence info
    r"Footnotes.*",  # Match footnotes section
    r"Publication\s*date.*",  # Match publication date metadata
    r"^'?[A-Z]\.\s*[A-Z]\.\s*,\s*[A-Z]\.\s*,\s*[A-Z]\.\s*,\s*.*?$",  # Matches fragmented entries
    # **Patterns to Match Individual Bibliographic Entries**
    # Pattern 1: Multiple initials followed by publisher and year
    r"(?i)(?:[A-Z]\.\s*){1,4},\s*[^,]+,\s*(?:"
    + "|".join(PUBLISHERS)
    + r"),\s*[^,]+,\s*\d{4},\s*\d+",
    # Pattern 2: Multiple initials and fragmented entries
    r"(?i)(?:[A-Z]\.\s*){1,4},\s*(?:and\s*)?(?:[A-Z]\.\s*)?,\s*[^,]+,\s*(?:"
    + "|".join(PUBLISHERS)
    + r"),\s*[^,]+,?",
    # Pattern 3: Publisher names followed by location and year
    r"(?i)" + "|".join(PUBLISHERS) + r",\s*\w+,\s*\d{4},\s*\d+",
    # Pattern 4: Patterns like "E. A., and J. ,"
    r"(?i)\b[A-Z]\.\s[A-Z]+\.\s*,\s*",
    # Pattern 5: Patterns like "15- ,"
    r"\b\d{1,3}-\s*,",
    r"©\s*\d{4}.*",  # Copyright
    r"Downloaded\s+from\s+\S+",  # Download notices
    r"Published\s+in\s+\S+",  # Publication info
    r"Corresponding\s+author:\s*\S+",  # Correspondence info,
    r"P\.?\s*O\.?\s*Box\s*\d+",  # P.O. Box patterns
    r"\d+\s*(?:Department|Institute|School|Faculty)\s+of\s+[A-Za-z\s]+,\s+[A-Za-z\s]+,\s+[A-Za-z\s]+(?:,\s+[A-Za-z\s]+)*",  # Flexible affiliations
    r"Received\s+\d{1,2}\s+\w+\s+\d{4};\s+published\s+\d{1,2}\s+\w+\s+\d{4}",  # Received/Published dates
    r"All rights reserved\..*?Downloaded from .*?\. See the Terms and Conditions.*",  # Rights and download notices
    r"\b[A-Za-z]{2}\s*\d{5}\b",  # Postal codes (e.g., "OX1 3PU")
    r"\bdoi:\s*10\.\d{4,9}/[-._;()/:A-Z0-9]+",
    r"-\n",  # Remove hyphenated line breaks
]


NX_TERM_BLACKLIST = [
    "nx",
    "inf",
    "classes",
    "nx_pylab",
    "defaultdict",
    "utils",
    "all",
    "exception",
    "duplication",
    "load",
    "islice",
    "draw networkx",
    "convert",
    "empty",
    "group",
    "draw",
    "layout",
    "text",
    "write_network_text",
    "write_edgelist",
    "write_gml",
    "write_graph6",
    "write_sparse6",
    "write_multiline_adjlist",
    "write_pajek",
    "write_weighted_edgelist",
    "write_graphml",
    "write_graphml_lxml",
    "read_graph6",
    "read_edgelist",
    "read_gml",
    "read_gexf",
    "read_multiline_adjlist",
    "read_pajek",
    "read_sparse6",
    "readwrite",
    "utils",
    "attr_matrix",
    "attr_sparse_matrix",
    "json_graph",
    "graphml",
    "GraphMLReader",
    "GraphMLWriter",
    "adjacency",
    "adjlist",
    "nx_agraph",
    "nx_latex",
    "nx_pydot",
    "nx_pylab",
    "graphml",
    "convert_matrix",
    "parse_adjlist",
    "parse_edgelist",
    "parse_graphml",
    "parse_gml",
    "parse_leda",
    "parse_pajek",
    "generate_adjlist",
    "generate_edgelist",
    "generate_multiline_adjlist",
    "generate_gml",
    "generate_graphml",
    "generate_pajek",
    "from_dict_of_dicts",
    "to_dict_of_dicts",
    "from_numpy_array",
    "to_numpy_array",
    "from_pandas_adjacency",
    "from_pandas_edgelist",
    "to_pandas_edgelist",
    "from_scipy_sparse_array",
    "to_scipy_sparse_array",
    "from_graph6_bytes",
    "to_graph6_bytes",
    "from_sparse6_bytes",
    "to_sparse6_bytes",
    "to_networkx_graph",
    "to_dict_of_lists",
    "to_latex",
    "to_latex_raw",
    "to_nested_tuple",
    "attrmatrix",
    "build_flow_dict",
    "generate_gexf",
    "combinations",
    "function",
    "reportviews",
    "config",
]
