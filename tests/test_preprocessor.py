"""Tests for ai_project.preprocessor."""

import pytest

from ai_project.preprocessor import extract_keywords, normalize, tokenize


class TestTokenize:
    def test_basic(self):
        assert tokenize("Hello World") == ["hello", "world"]

    def test_punctuation_removed(self):
        assert tokenize("Hello, world!") == ["hello", "world"]

    def test_empty_string(self):
        assert tokenize("") == []

    def test_numbers_kept(self):
        assert tokenize("There are 3 apples") == ["there", "are", "3", "apples"]


class TestNormalize:
    def test_trims_whitespace(self):
        assert normalize("  hello  ") == "hello"

    def test_collapses_spaces(self):
        assert normalize("hello   world") == "hello world"

    def test_newlines_collapsed(self):
        assert normalize("hello\n\nworld") == "hello world"

    def test_empty_string(self):
        assert normalize("") == ""


class TestExtractKeywords:
    def test_removes_stop_words(self):
        keywords = extract_keywords("The cat is on the mat")
        assert "the" not in keywords
        assert "is" not in keywords
        assert "on" not in keywords

    def test_returns_unique_words(self):
        keywords = extract_keywords("cat cat dog dog")
        assert keywords.count("cat") == 1
        assert keywords.count("dog") == 1

    def test_custom_stop_words(self):
        keywords = extract_keywords("cat and dog", stop_words=["and"])
        assert "and" not in keywords
        assert "cat" in keywords
        assert "dog" in keywords

    def test_empty_string(self):
        assert extract_keywords("") == []
