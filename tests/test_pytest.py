from mock import MagicMock

import pytest

import main_app

WORD = 'skillfactory'
GUESSED = False
TRIES = 6


def test_str_upper_answer():
    word = main_app.WORD
    if word == '' or word is None:
        assert word


def test_boolean_game_result():
    if not main_app.game or main_app.game is None:
        assert main_app.game is None
