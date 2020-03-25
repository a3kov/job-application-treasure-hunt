from functional import get_clues
from lib import TEST_INPUT, TEST_RESULT


def test_get_clues():
    gen = get_clues(TEST_INPUT)
    assert tuple(gen) == TEST_RESULT
