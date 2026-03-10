"""Simple keyword-based intent classifier."""

from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Built-in intent patterns
# ---------------------------------------------------------------------------
DEFAULT_INTENTS: Dict[str, List[str]] = {
    "greeting": ["hello", "hi", "hey", "greetings", "howdy", "good morning", "good afternoon", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "take care", "later", "farewell"],
    "thanks": ["thank", "thanks", "thank you", "appreciate", "grateful"],
    "help": ["help", "assist", "support", "how do", "what can", "guide"],
    "weather": ["weather", "temperature", "forecast", "rain", "sunny", "cloudy", "snow"],
    "time": ["time", "clock", "hour", "minute", "what time"],
    "name": ["your name", "who are you", "what are you", "introduce"],
}


class IntentClassifier:
    """Classify user input into one of a set of known intents.

    Parameters
    ----------
    intents:
        A mapping of intent label → list of trigger phrases/keywords.
        Defaults to :data:`DEFAULT_INTENTS`.
    """

    def __init__(self, intents: Optional[Dict[str, List[str]]] = None) -> None:
        self.intents: Dict[str, List[str]] = intents if intents is not None else DEFAULT_INTENTS

    def classify(self, text: str) -> str:
        """Return the most likely intent for *text*, or ``"unknown"`` if no intent matches.

        The classifier scores each intent by counting how many of its keywords
        appear in the lowercased *text*, then returns the highest-scoring label.

        Args:
            text: The raw user input string.

        Returns:
            The predicted intent label.
        """
        lowered = text.lower()
        best_intent = "unknown"
        best_score = 0

        for intent, keywords in self.intents.items():
            score = sum(1 for kw in keywords if kw in lowered)
            if score > best_score:
                best_score = score
                best_intent = intent

        return best_intent

    def add_intent(self, label: str, keywords: List[str]) -> None:
        """Register a new intent (or extend an existing one) with *keywords*.

        Args:
            label: The intent label to add or update.
            keywords: A list of trigger phrases for the intent.
        """
        if label in self.intents:
            self.intents[label] = list(set(self.intents[label] + keywords))
        else:
            self.intents[label] = keywords
