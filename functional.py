from lib import get_input


def get_clues(input):
    tens = 1
    units = 1
    row = col = None
    item = 11
    while tens != row or units != col:
        yield item
        row = tens
        col = units
        item = input[row - 1][col - 1]
        tens = item // 10
        units = item - (tens * 10)


if __name__ == '__main__':
    input = get_input()
    print(' '.join(map(str, get_clues(input))))
