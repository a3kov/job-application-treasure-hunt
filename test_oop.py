from oop import search, Item
from lib import TEST_INPUT, TEST_RESULT


def test_search():
    clues = search(Item(TEST_INPUT, 1, 1))
    clue_numbers = [x.clue for x in clues]
    assert tuple(clue_numbers) == TEST_RESULT


def test_item():
    item = Item(TEST_INPUT, 1, 1)
    assert item.number == 55


def test_item_is_treasure():
    assert Item(TEST_INPUT, 4, 3).is_treasure is True
    for row in range(5):
        for col in range(5):
            if row != 4 or col != 3:
                assert Item(TEST_INPUT, row, col).is_treasure is not True


def test_item_next():
    item = Item(TEST_INPUT, 1, 1)
    assert item.next().clue == 55
