import pytest

import main_app

WORD = 'skillfactory'


@pytest.fixture()
def get_answers():
    main_app.get_word = WORD.upper()
