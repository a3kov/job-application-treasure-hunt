from lib import get_input


class Item:
    def __init__(self, table, row, col):
        self.table = table
        self.row = row
        self.col = col
        self.clue = self.row * 10 + self.col
        self.number = table[row - 1][col - 1]
        self._tens = self.number // 10
        self._units = self.number - (self._tens * 10)

    @property
    def is_treasure(self):
        return self.row == self._tens and self.col == self._units

    def next(self):
        return Item(self.table, self._tens, self._units)


def search(item):
    items = [item]
    if not item.is_treasure:
        items += search(item.next())
    return items


if __name__ == '__main__':
    input = get_input()
    clues = search(Item(input, 1, 1))
    print(' '.join([str(x.clue) for x in clues]))
