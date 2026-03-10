"""Tests for ai_project.chatbot."""

import pytest

from ai_project.chatbot import Chatbot
from ai_project.classifier import IntentClassifier


class TestChatbot:
    def setup_method(self):
        self.bot = Chatbot()

    def test_respond_returns_string(self):
        response = self.bot.respond("Hello!")
        assert isinstance(response, str)
        assert len(response) > 0

    def test_greeting_response(self):
        response = self.bot.respond("Hello!")
        # Any of the greeting responses should be returned
        assert response in self.bot.responses["greeting"]

    def test_history_recorded(self):
        self.bot.respond("Hello!")
        assert len(self.bot.history) == 2
        assert self.bot.history[0]["role"] == "user"
        assert self.bot.history[1]["role"] == "assistant"

    def test_history_content(self):
        self.bot.respond("  Hello!  ")
        assert self.bot.history[0]["content"] == "Hello!"

    def test_reset_clears_history(self):
        self.bot.respond("Hello!")
        self.bot.reset()
        assert self.bot.history == []

    def test_cycles_through_responses(self):
        # The bot should cycle through the available greeting responses
        num_responses = len(self.bot.responses["greeting"])
        seen = set()
        for _ in range(num_responses * 2):
            seen.add(self.bot.respond("hi"))
        # All greeting responses should have been used at least once
        assert seen == set(self.bot.responses["greeting"])

    def test_custom_name(self):
        bot = Chatbot(name="Buddy")
        assert bot.name == "Buddy"

    def test_unknown_intent_fallback(self):
        response = self.bot.respond("xyzzy gobbledygook 12345")
        assert response in self.bot.responses["unknown"]

    def test_custom_responses(self):
        custom = {"greeting": ["Yo!"], "unknown": ["No idea."]}
        bot = Chatbot(responses=custom)
        assert bot.respond("hello") == "Yo!"

    def test_whitespace_normalised(self):
        r1 = Chatbot().respond("  Hello   ")
        r2 = Chatbot().respond("Hello")
        assert r1 == r2
