"""Text preprocessing utilities for the AI project."""

import re
import string
from typing import List


def tokenize(text: str) -> List[str]:
    """Split text into a list of word tokens (lowercased, punctuation removed).

    Args:
        text: The input string to tokenize.

    Returns:
        A list of lowercase word tokens.
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def normalize(text: str) -> str:
    """Normalize whitespace and strip leading/trailing spaces.

    Args:
        text: The input string to normalize.

    Returns:
        The normalized string.
    """
    return re.sub(r"\s+", " ", text).strip()


def extract_keywords(text: str, stop_words: List[str] | None = None) -> List[str]:
    """Return unique keywords from *text*, excluding common stop words.

    Args:
        text: The input string to extract keywords from.
        stop_words: Optional list of words to exclude.  When *None* a small
            built-in list of English stop words is used.

    Returns:
        A deduplicated list of keyword tokens (order preserved).
    """
    if stop_words is None:
        stop_words = [
            "a", "an", "the", "is", "it", "in", "on", "at", "to", "of",
            "and", "or", "but", "for", "with", "that", "this", "was", "are",
        ]
    tokens = tokenize(normalize(text))
    seen: set[str] = set()
    keywords: List[str] = []
    for token in tokens:
        if token not in stop_words and token not in seen:
            seen.add(token)
            keywords.append(token)
    return keywords
