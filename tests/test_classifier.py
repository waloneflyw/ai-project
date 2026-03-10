"""Tests for ai_project.classifier."""

import pytest

from ai_project.classifier import IntentClassifier


class TestIntentClassifier:
    def setup_method(self):
        self.clf = IntentClassifier()

    def test_greeting(self):
        assert self.clf.classify("Hello there!") == "greeting"

    def test_farewell(self):
        assert self.clf.classify("Goodbye, see you later") == "farewell"

    def test_thanks(self):
        assert self.clf.classify("Thank you very much") == "thanks"

    def test_unknown(self):
        assert self.clf.classify("xyzzy irrelevant gobbledygook") == "unknown"

    def test_add_new_intent(self):
        self.clf.add_intent("joke", ["joke", "funny", "laugh"])
        assert self.clf.classify("Tell me a funny joke") == "joke"

    def test_extend_existing_intent(self):
        self.clf.add_intent("greeting", ["salutation"])
        assert self.clf.classify("salutation everyone") == "greeting"

    def test_custom_intents(self):
        clf = IntentClassifier(intents={"color": ["red", "blue", "green"]})
        assert clf.classify("I like blue") == "color"
        assert clf.classify("hello") == "unknown"
