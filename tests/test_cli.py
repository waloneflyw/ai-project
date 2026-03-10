"""Tests for ai_project.cli."""

import pytest

from ai_project.cli import build_parser, main


class TestCLI:
    def test_version(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "0.1.0" in captured.out

    def test_single_message(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            main(["--message", "Hello!"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert len(captured.out.strip()) > 0

    def test_single_message_short_flag(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            main(["-m", "Thank you"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert len(captured.out.strip()) > 0

    def test_custom_name_flag(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            main(["--name", "Buddy", "--message", "hi"])
        assert exc_info.value.code == 0
