from lib import get_row, get_input, TEST_INPUT
from unittest.mock import Mock


def test_get_row():
    assert get_row(lambda x: "11 22 33", 1) is None
    assert get_row(lambda x: "11 22 33 4g 55", 1) is None
    assert get_row(lambda x: "11 22 33 44 55 66", 1) is None
    assert get_row(lambda x: "11 22 33 44  55", 1) is None
    assert get_row(lambda x: "11 22 33 44 55 ", 1) is None
    assert get_row(lambda x: "11 22 33 44 55", 1) == (11, 22, 33, 44, 55)


def test_get_input():
    text_input = TEST_INPUT[:3] + (None,) + TEST_INPUT[3:]
    get_row = Mock(side_effect=text_input)
    print_func = Mock()
    result = get_input(get_row_func=get_row, print_func=print_func)
    assert result == TEST_INPUT
    assert get_row.call_count == 6
    assert print_func.call_count == 1
