'''
Solve the problem of puzzle game
github: https://github.com/VictoriyaRoy/puzzle
'''
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


def column_check(board: list) -> bool:
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
    >>> column_check(board)
    False
    >>> column_check([])
    True
    '''
    new_board = ['' for _ in range(9)]
    for line in board:
        for index, element in enumerate(line):
            new_board[index] += element
    return row_check(new_board)


def format_board(board: list) -> list:
    '''
    Format board by removing all stars
    >>> format_board(['*3*', '**2', '*87'])
    ['3', '2', '87']
    >>> format_board([])
    []
    '''
    new_board = []
    for line in board:
        new_board.append(line.replace('*', ''))
    return new_board


def color_check(board: list) -> list:
    '''
    Check if in each color area there are numbers from 1 to 9 without repetitions
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
    >>> color_check(board)
    True
    >>> color_check([])
    True
    '''
    board = format_board(board)
    color_board = ['' for _ in range(5)]
    for color in range(5):
        for line in board:
            if line:
                color_board[color] += (line[-1])
                line = line[:-1]
    return row_check(color_board)


def validate_board(board: list) -> bool:
    '''
    Check if board meets the rules
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
    >>> validate_board(board)
    False
    >>> validate_board([])
    True
    '''
    return row_check(board) and column_check(board) and color_check(board)


if __name__ == '__main__':
    from doctest import testmod
    print(testmod())
