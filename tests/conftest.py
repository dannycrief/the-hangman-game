import pytest

import main_app

WORD = 'skillfactory'
GUESSED = False
GUESSED_LETTERS = []
GUESSED_WORDS = []
TRIES = 6


@pytest.fixture()
def get_answers():
    main_app.get_word = WORD.upper()
