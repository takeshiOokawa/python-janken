"""じゃんけんゲームの自動テスト"""
import io
from unittest.mock import patch

import pytest

from janken import (
    CHOICES, DRAW, GUU, CHOKI, PAA, LOSE, WIN,
    get_cpu_choice, get_player_choice, judge, play_again, show_score,
)


# --- judge() ---

class TestJudge:
    def test_draw(self):
        assert judge(GUU, GUU) == DRAW
        assert judge(CHOKI, CHOKI) == DRAW
        assert judge(PAA, PAA) == DRAW

    def test_win(self):
        assert judge(GUU, CHOKI) == WIN
        assert judge(CHOKI, PAA) == WIN
        assert judge(PAA, GUU) == WIN

    def test_lose(self):
        assert judge(GUU, PAA) == LOSE
        assert judge(CHOKI, GUU) == LOSE
        assert judge(PAA, CHOKI) == LOSE


# --- get_cpu_choice() ---

class TestGetCpuChoice:
    def test_returns_valid_choice(self):
        for _ in range(20):
            assert get_cpu_choice() in CHOICES

    def test_all_choices_possible(self):
        results = {get_cpu_choice() for _ in range(200)}
        assert results == set(CHOICES)


# --- get_player_choice() ---

class TestGetPlayerChoice:
    @pytest.mark.parametrize("inp,expected", [
        ("1", GUU), ("グー", GUU), ("ぐー", GUU), ("ぐ", GUU), ("グ", GUU),
        ("2", CHOKI), ("チョキ", CHOKI), ("ちょき", CHOKI),
        ("3", PAA), ("パー", PAA), ("ぱー", PAA),
    ])
    def test_valid_inputs(self, inp, expected):
        with patch("builtins.input", return_value=inp):
            assert get_player_choice() == expected

    def test_invalid_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["あ", "rock", "", "1"]):
            result = get_player_choice()
        assert result == GUU
        captured = capsys.readouterr()
        assert "無効な入力" in captured.out

    def test_empty_input_reprompts(self, capsys):
        with patch("builtins.input", side_effect=["", "2"]):
            result = get_player_choice()
        assert result == CHOKI


# --- play_again() ---

class TestPlayAgain:
    def test_y_returns_true(self):
        with patch("builtins.input", return_value="y"):
            assert play_again() is True

    def test_n_returns_false(self):
        with patch("builtins.input", return_value="n"):
            assert play_again() is False

    def test_invalid_then_valid(self, capsys):
        with patch("builtins.input", side_effect=["a", "yes", "n"]):
            result = play_again()
        assert result is False
        assert "y」か「n」" in capsys.readouterr().out


# --- show_score() ---

class TestShowScore:
    def test_normal(self, capsys):
        show_score({WIN: 3, LOSE: 1, DRAW: 1})
        out = capsys.readouterr().out
        assert "総対戦数: 5回" in out
        assert "勝ち: 3回" in out
        assert "60.0%" in out

    def test_zero_games_no_zerodivision(self, capsys):
        show_score({WIN: 0, LOSE: 0, DRAW: 0})
        out = capsys.readouterr().out
        assert "総対戦数: 0回" in out
        assert "0.0%" in out
