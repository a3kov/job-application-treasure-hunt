import re

ROW_PATTERN = (
    r"([1-5][1-5]) ([1-5][1-5]) ([1-5][1-5]) ([1-5][1-5]) ([1-5][1-5])"
)
TEST_INPUT = (
    (55, 14, 25, 52, 21),
    (44, 31, 11, 53, 43),
    (24, 13, 45, 12, 34),
    (42, 22, 43, 32, 41),
    (51, 23, 33, 54, 15),
)
TEST_RESULT = (11, 55, 15, 21, 44, 32, 13, 25, 43)


def get_row(input_func, row_num):
    row_str = input_func(f"Please enter row {row_num}:")
    match = re.fullmatch(ROW_PATTERN, row_str)
    if match is not None:
        return tuple(map(int, match.groups()))


def get_input(get_row_func=get_row, print_func=print):
    data = []
    for x in range(1, 6):
        row = None
        while row is None:
            row = get_row_func(input, x)
            if row is None:
                print_func("\nIncorrect input: row should be 5 two digit "
                           "numbers separated by single spaces.\n")
        data.append(row)
    return tuple(data)
