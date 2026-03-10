# ai-project

A lightweight, dependency-free conversational AI assistant written in Python.

## Features

- **Intent classification** – keyword-based engine that maps user input to named intents
- **Chatbot** – cycling response system with conversation history
- **Text preprocessing** – tokenization, whitespace normalization, keyword extraction
- **CLI** – interactive REPL and single-message (`-m`) modes

## Installation

```bash
pip install -e .
```

## Quick start

### Interactive mode

```bash
ai-project
```

```
AI Assistant: Hello! Type 'quit' or 'exit' to stop.

You: Hello!
AI Assistant: Hello! How can I help you today?

You: quit
AI Assistant: Goodbye!
```

### Single-message mode

```bash
ai-project -m "Hello!"
# Hello! How can I help you today?
```

### Python API

```python
from ai_project.chatbot import Chatbot

bot = Chatbot(name="Buddy")
print(bot.respond("Hello!"))   # Hello! How can I help you today?
print(bot.respond("Thanks"))   # You're welcome!
```

## Project structure

```
src/ai_project/
├── __init__.py       # package version
├── preprocessor.py   # tokenize / normalize / extract_keywords
├── classifier.py     # IntentClassifier
├── chatbot.py        # Chatbot
└── cli.py            # CLI entry-point

tests/
├── test_preprocessor.py
├── test_classifier.py
├── test_chatbot.py
└── test_cli.py
```

## Development

```bash
pip install -e .
pip install pytest
pytest
```

## License

MIT
