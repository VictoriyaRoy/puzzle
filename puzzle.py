def row_check(board: list) -> bool:
    '''
    Check if in each rows there are numbers from 1 to 9 without repetitions
    >>> board = [\
    "**** ****", \
    "***1 ****", \
    "**  3****", \
    "* 4 1****", \
    "     9 5 ", \
    " 6  83  *", \
    "3   1  **", \
    "  8  2***", \
    "  2  ****"]
    >>> row_check(board)
    True
    >>> row_check([])
    True
    '''

    for line in board:
        new_line = line.replace('*', '').replace(' ', '')
        if len(new_line) != len(set(new_line)):
            return False
    return True


if __name__ == '__main__':
    from doctest import testmod
    print(testmod())
