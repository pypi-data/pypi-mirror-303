import warnings
from collections.abc import Callable
from enum import Enum

import numpy as np

from _nxlu.config import NxluConfig, _config

from _nxlu.enums import (  # isort: skip # noqa: F401
    AnthropicModel,
    LocalModel,
    OpenAIModel,
    Framework,
)

warnings.filterwarnings("ignore")


def get_config() -> NxluConfig:
    """Return the singleton configuration instance."""
    return _config


CostFunction = Callable[[int, int], float]

COMPLEXITY_COST_MAPPING: dict[str, CostFunction] = {
    "constant": lambda n, m: 1.0,  # O(1)
    "logarithmic": lambda n, m: np.log(n),  # O(log n)
    "linear": lambda n, m: n,  # O(n)
    "linear + m": lambda n, m: n + m,  # O(n + m)
    "linear * m": lambda n, m: n * m,  # O(n * m)
    "loglinear": lambda n, m: n * np.log(n),  # O(n log n)
    "linear + loglinear": lambda n, m: n + n * np.log(n),  # O(n + n log n)
    "linear * m + loglinear": lambda n, m: n * m + n * np.log(n),  # O(n(m + n log n))
    "quadratic": lambda n, m: n**2,  # O(n^2)
    "polynomial": lambda n, m: n**2 + m,  # O(n^2 + m)
    "quadratic + nm": lambda n, m: n**2 + n * m,  # O(n^2 + n*m)
    "quadratic * m": lambda n, m: n**2 * m,  # O(n^2 * m)
    "logquadratic + nm": lambda n, m: n**2 * np.log(n) + n * m,  # O(NM + N^2 log N)
    "cubic": lambda n, m: n**3,  # O(n^3)
    "cubic + m": lambda n, m: n**3 + m,  # O(n^3 + m)
    "exponential": lambda n, m: 2**n,  # O(2^n)
}


class RescalingMethod(str, Enum):
    normalize = "normalize"
    standardize = "standardize"
    invert = "invert"
    binarize = "binarize"


class Intent(Enum):
    # 1. Information Seeking and Retrieval
    FACT_RETRIEVAL = "Fact Retrieval"
    CLARIFICATION = "Clarification"
    CONTEXTUAL_SEARCH = "Contextual Search"
    VERIFICATION = "Verification"
    EXPLORATION = "Exploration"

    # 2. Reasoning and Explanation
    CAUSAL_EXPLANATION = "Causal Explanation"
    PROCEDURAL_EXPLANATION = "Procedural Explanation"
    CONCEPTUAL_EXPLANATION = "Conceptual Explanation"
    COMPARATIVE_EXPLANATION = "Comparative Explanation"
    SEQUENTIAL_REASONING = "Sequential Reasoning"

    # 3. Decision-Making and Recommendations
    RECOMMENDATION = "Recommendation"
    PRIORITIZATION = "Prioritization"
    DECISION_SUPPORT = "Decision Support"
    ACTION_SUGGESTION = "Action Suggestion"
    ALTERNATIVES_EXPLORATION = "Alternatives Exploration"

    # 4. Diagnostic and Analytical
    DIAGNOSTIC_REASONING = "Diagnostic Reasoning"
    ROOT_CAUSE_ANALYSIS = "Root Cause Analysis"
    ERROR_DETECTION = "Error Detection"
    FAULT_IDENTIFICATION = "Fault Identification"
    PATTERN_RECOGNITION = "Pattern Recognition"

    # 5. Instruction and Guidance
    STEP_BY_STEP_GUIDANCE = "Step-by-Step Guidance"
    TASK_COMPLETION = "Task Completion"
    PROCESS_OPTIMIZATION = "Process Optimization"
    TROUBLESHOOTING = "Troubleshooting"

    # 6. Creative and Ideation
    IDEA_GENERATION = "Idea Generation"
    CONTENT_CREATION = "Content Creation"
    BRAINSTORMING = "Brainstorming"
    STORYTELLING = "Storytelling"

    # 7. Classification and Categorization
    CATEGORIZATION = "Categorization"
    CLASSIFICATION = "Classification"
    TAGGING = "Tagging"
    SORTING = "Sorting"

    # 8. Summarization and Information Condensation
    SUMMARIZATION = "Summarization"
    ABSTRACTION = "Abstraction"
    HIGHLIGHTING = "Highlighting"

    # 9. Personalization and Adaptation
    PERSONALIZATION = "Personalization"
    CUSTOMIZATION = "Customization"
    CONTEXTUAL_ADAPTATION = "Contextual Adaptation"

    # 10. Planning and Scheduling
    PLANNING = "Planning"
    GOAL_SETTING = "Goal Setting"
    SCHEDULING = "Scheduling"

    # 11. Navigation and Direction
    LOCATION_BASED_NAVIGATION = "Location-Based Navigation"
    RESOURCE_NAVIGATION = "Resource Navigation"
    PATHFINDING = "Pathfinding"

    # 12. Prediction and Forecasting
    PREDICTION = "Prediction"
    TREND_ANALYSIS = "Trend Analysis"
    FORECASTING = "Forecasting"
    OUTCOME_ESTIMATION = "Outcome Estimation"

    # 13. Problem-Solving and Strategy
    PROBLEM_SOLVING = "Problem Solving"
    STRATEGY_DEVELOPMENT = "Strategy Development"
    OPTIMIZATION = "Optimization"
    RISK_ASSESSMENT = "Risk Assessment"

    # 14. Collaboration and Coordination
    COLLABORATION = "Collaboration"
    TASK_DELEGATION = "Task Delegation"
    SYNCHRONIZATION = "Synchronization"
    SHARING = "Sharing"

    # 15. Miscellaneous High-Level Intents
    EMOTION_ANALYSIS = "Emotion Analysis"
    FEEDBACK = "Feedback"
