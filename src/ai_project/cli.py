"""Command-line interface for the AI assistant."""

import argparse
import sys

from . import __version__
from .chatbot import Chatbot


def build_parser() -> argparse.ArgumentParser:
    """Return a configured argument parser."""
    parser = argparse.ArgumentParser(
        prog="ai-project",
        description="AI Assistant – a simple conversational AI chatbot.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--name",
        default="AI Assistant",
        help="Display name for the assistant (default: 'AI Assistant').",
    )
    parser.add_argument(
        "--message",
        "-m",
        help="Send a single message and print the response (non-interactive mode).",
    )
    return parser


def interactive_loop(bot: Chatbot) -> None:
    """Run the interactive REPL until the user quits."""
    print(f"{bot.name}: Hello! Type 'quit' or 'exit' to stop.\n")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{bot.name}: Goodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit"}:
            print(f"{bot.name}: Goodbye!")
            break

        response = bot.respond(user_input)
        print(f"{bot.name}: {response}\n")


def main(argv: list | None = None) -> None:
    """Entry point for the ``ai-project`` CLI command."""
    parser = build_parser()
    args = parser.parse_args(argv)

    bot = Chatbot(name=args.name)

    if args.message:
        # Non-interactive: print one response and exit.
        print(bot.respond(args.message))
        sys.exit(0)

    interactive_loop(bot)


if __name__ == "__main__":
    main()
