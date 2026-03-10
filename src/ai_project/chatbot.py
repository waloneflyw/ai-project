"""Conversational AI assistant."""

import datetime
from typing import Dict, List, Optional

from .classifier import IntentClassifier
from .preprocessor import normalize


# ---------------------------------------------------------------------------
# Default response templates
# ---------------------------------------------------------------------------
DEFAULT_RESPONSES: Dict[str, List[str]] = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Nice to meet you. How can I assist?",
    ],
    "farewell": [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! Feel free to come back anytime.",
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime! Let me know if you need anything else.",
    ],
    "help": [
        "I can chat with you, answer questions, and help with various tasks. What do you need?",
        "Sure, I'm here to help! What would you like to know?",
    ],
    "weather": [
        "I don't have access to real-time weather data, but you can check a weather service for the latest forecast.",
    ],
    "time": [
        "The current time is {time}.",
    ],
    "name": [
        "I'm an AI assistant built with the ai-project library.",
        "You can call me AI Assistant. Nice to meet you!",
    ],
    "unknown": [
        "I'm not sure I understood that. Could you rephrase?",
        "Interesting! Tell me more.",
        "I don't have information on that topic yet.",
    ],
}


class Chatbot:
    """A simple keyword-intent-based conversational assistant.

    Parameters
    ----------
    name:
        Display name for the assistant (used in the CLI).
    responses:
        Mapping of intent → list of response strings.  When *None* the
        built-in :data:`DEFAULT_RESPONSES` are used.
    classifier:
        A pre-configured :class:`~ai_project.classifier.IntentClassifier`.
        When *None* a default instance is created automatically.
    """

    def __init__(
        self,
        name: str = "AI Assistant",
        responses: Optional[Dict[str, List[str]]] = None,
        classifier: Optional[IntentClassifier] = None,
    ) -> None:
        self.name = name
        self.responses: Dict[str, List[str]] = responses if responses is not None else DEFAULT_RESPONSES
        self.classifier: IntentClassifier = classifier if classifier is not None else IntentClassifier()
        self._response_indices: Dict[str, int] = {}
        self.history: List[Dict[str, str]] = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def respond(self, user_input: str) -> str:
        """Generate a response to *user_input*.

        The method normalises the text, classifies the intent, selects the
        next response for that intent (cycling through the list), and records
        the exchange in :attr:`history`.

        Args:
            user_input: Raw text from the user.

        Returns:
            The assistant's reply as a string.
        """
        clean_input = normalize(user_input)
        intent = self.classifier.classify(clean_input)
        response = self._pick_response(intent)

        self.history.append({"role": "user", "content": clean_input})
        self.history.append({"role": "assistant", "content": response})

        return response

    def reset(self) -> None:
        """Clear the conversation history and reset response cycle indices."""
        self.history.clear()
        self._response_indices.clear()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _pick_response(self, intent: str) -> str:
        """Return the next response for *intent*, cycling through the list."""
        options = self.responses.get(intent, self.responses.get("unknown", ["I don't know."]))
        idx = self._response_indices.get(intent, 0)
        response = options[idx % len(options)]
        self._response_indices[intent] = idx + 1
        # Substitute dynamic placeholders.
        if "{time}" in response:
            response = response.replace("{time}", datetime.datetime.now().strftime("%H:%M"))
        return response
