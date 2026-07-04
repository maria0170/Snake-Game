from constants import (
    DOWN,
    EMPTY,
    FOOD,
    HEAD,
    LEFT,
    RIGHT,
    SNAKE_BODY,
    UP,
)


def make_board(width: int, height: int) -> list[list[str]]:
    """Return a new board with width columns and height rows.
    The returned board is a nested list of strings filled with the
    character ".". The board uses row-major layout:
    board[y][x] refers to column x in row y.

    The board contains exactly height rows, and each row contains
    exactly width columns.

    If width == 0 or height == 0, return [].

    Preconditions:
    - width >= 0
    - height >= 0

    >>> make_board(3, 2)
    [['.', '.', '.'], ['.', '.', '.']]

    >>> make_board(0,0)
    []

    >>> make_board(1, 4)
    [['.'], ['.'], ['.'], ['.']]

    """
    # Replace pass with your function body
    if width == 0 or height == 0:
        return []

    board = []
    num_width = 0

    if width > num_width:
        board.append(width * [EMPTY])

    num_height = 0
    if height > num_height:
        for multiply in range(height - 1):
            multiply = []
            multiply.append(width * [EMPTY])
            board.extend(multiply)

    return board


# =======Add the rest of functions here=========
# ===================================

def clear_board(board: list[list[str]]) -> None:
    """ Return a modified board such that every sell is replaced with '.'

    >>> b = [['S', 'S'], ['F', '.']]
    >>> clear_board(b)
    >>> b
    [['.', '.'], ['.', '.']]

    >>> a = [['S'], ['F']]
    >>> clear_board(a)
    >>> a
    [['.'], ['.']]


    """
    for row in board:
        for i in range(len(row)):
            row[i] = EMPTY


def place_snake_and_food(board: list[list[str]], snake: list[list[int]],
                         food: list[int]) -> None:
    """ A modified board that displays the snake and food

    The snake is a list of [x, y] coordinates.
    The first coordinate is the head ("H").
    All other segments are body ("S").
    The food is marked as "F".
    The snake and the food are at a valid location in the board.

    >>> b = make_board(4, 3)
    >>> snake = [[1, 1], [0, 1], [0, 2]]
    >>> food = [3, 0]
    >>> place_snake_and_food(b, snake, food)
    >>> b
    [['.', '.', '.', 'F'], ['S', 'H', '.', '.'], ['S', '.', '.', '.']]

    >>> a = make_board(3, 4)
    >>> snake = [[0, 1], [1, 1], [2, 2]]
    >>> food = [2, 1]
    >>> place_snake_and_food(a, snake, food)
    >>> a
    [['.', '.', '.'], ['H', 'S', 'F'], ['.', '.', 'S'], ['.', '.', '.']]
    """

    clear_board(board)

    board[food[1]][food[0]] = FOOD

    for i in range(len(snake)):
        x = snake[i][0]
        y = snake[i][1]

        if i == 0:
            board[y][x] = HEAD
        else:
            board[y][x] = SNAKE_BODY


def single_cell(row: list[str]) -> list[str]:
    """Return a list representing a single row with spaces between the cells.

    >>> single_cell(['S','H', '.', 'S'])
    ['S', ' ', 'H', ' ', '.', ' ', 'S']

    >>> single_cell(['.'])
    ['.']

    >>> single_cell(['H', 'S'])
    ['H', ' ', 'S']

    """
    row_collect = []

    for i in range(len(row)):
        row_collect.append(row[i])
        if i != len(row) - 1:
            row_collect.append(' ')
    return row_collect


def board_to_string(board: list[list[str]]) -> str:
    """Return a representation of the board, with each row appears in a new
    line and cells in a row are separated by a sinlge space. Where the rows
    are separated by '\n'.

    >>> b = [['H', 'S', '.'], ['.', 'F', '.']]
    >>> board_to_string(b)
    'H S .\\n. F .'

    >>> a = [['S','H','.','S']]
    >>> board_to_string(a)
    'S H . S'

    >>> c = [['.']]
    >>> board_to_string(c)
    '.'

    """

    board_return = []

    for i in range(len(board)):
        board_return.extend(single_cell(board[i]))
        if i != len(board) - 1:
            board_return.append('\n')

    result = ''
    for item in board_return:
        result = result + item

    return result


def snake_as_pairs(snake_xs: list[int], snake_ys: list[int]) -> list[list[int]]:
    """ Return [x,y] coordinate pairs created from the two paired lists
    snake_xs and snake_ys.

    Precondition : snake_xs and snake_ys have the same length, and the head
    appears first

    >>> snake_as_pairs([5, 4, 3], [2, 2, 2])
    [[5, 2], [4, 2], [3, 2]]

    >>> snake_as_pairs([],[])
    []

    >>> snake_as_pairs([1],[2])
    [[1, 2]]

    >>> snake_as_pairs([1,2,3,4], [5,6,7,8])
    [[1, 5], [2, 6], [3, 7], [4, 8]]

    """
    snakes = []

    if len(snake_xs) == len(snake_ys):
        for i in range(len(snake_xs)):
            snakes.append([snake_xs[i], snake_ys[i]])

    return snakes


def check_self_collision(snake_xs: list[int], snake_ys: list[int]) -> bool:
    """Return True if the hand overlaps any body segments, in snake_xs and
    snake_ys.

    Precondition : snake_xs and snake_ys have the same length and the head
    appears first

    >>> check_self_collision([2, 1, 2], [2, 2, 2])
    True

    >>> check_self_collision([2, 1, 0], [2, 2, 2])
    False

    >>> check_self_collision([],[])
    False

    """
    if snake_xs == [] and snake_ys == []:
        return False

    head_x = snake_xs[0]
    head_y = snake_ys[0]
    for i in range(1, len(snake_xs)):
        if head_x == snake_xs[i] and head_y == snake_ys[i]:
            return True
    return False


def move_snake(snake_xs: list[int], snake_ys: list[int], dx: int, dy: int,
               width: int, height: int, food: list[int]) -> bool:
    """Return True if the new head postion of the snake after one step
    using dx, dy has wrapped around past the grid edge of snake_xs, snake_ys
    and reapperaed on the opposite side in width and height, matches the food
    and the snake grows.

    >>> xs, ys = [2, 1, 0], [0, 0, 0]
    >>> move_snake(xs, ys, 1, 0, 5, 5, [4, 4])
    False
    >>> xs, ys
    ([3, 2, 1], [0, 0, 0])

    # Wrap-around example:

    >>> xs, ys = [0, 1], [0, 0]
    >>> move_snake(xs, ys, -1, 0, 3, 3, [4, 4])
    False
    >>> xs, ys
    ([2, 0], [0, 0])

    """
    head_x = snake_xs[0]
    head_y = snake_ys[0]

    new_x = head_x + dx
    new_y = head_y + dy

    new_x = new_x % width
    new_y = new_y % height

    snake_xs.insert(0, new_x)
    snake_ys.insert(0, new_y)

    if new_x == food[0] and new_y == food[1]:
        return True

    snake_xs.pop()
    snake_ys.pop()

    return False


def update_direction(curr_dx: int, curr_dy: int, key: str) -> list[int]:
    """Return a new direction after arrow key press, the curr_dx and
    curr_dy are the current direction; the keys are up,down,left,right and if
    the direction is exact opposite of the currect direction, return the
    originial direction unchanged.

    >>> update_direction(1, 0, UP)
    [0, -1]

    >>> update_direction(0, 1, DOWN)
    [0, 1]

    >>> update_direction(0, -1, 'B')
    [0, -1]

    """

    if key not in (UP, DOWN, LEFT, RIGHT):
        return [curr_dx, curr_dy]

    new_x, new_y = curr_dx, curr_dy

    if key == UP:
        new_x, new_y = 0, -1
    elif key == RIGHT:
        new_x, new_y = 1, 0
    elif key == DOWN:
        new_x, new_y = 0, 1
    elif key == LEFT:
        new_x, new_y = -1, 0

    if (curr_dx == - new_x) or (curr_dy == - new_y):
        return [curr_dx, curr_dy]

    return [new_x, new_y]


def would_collide_after_move(snake_xs: list[int], snake_ys: list[int], dx: int,
                             dy: int, width: int, height: int) -> bool:
    """Return True if and only if moving the head by (dx, dy) would land on
    a body segment (with wrap-around) of snake_xs and snake_ys where width and
    height are used for the collision.. False when there is no collision.

    # left into body
    >>> would_collide_after_move([5, 4, 3], [0, 0, 0], -1, 0, 10, 10)
    True

    # right, no body
    >>> would_collide_after_move([5, 4, 3], [0, 0, 0], 1, 0, 10, 10)
    False

    >>> would_collide_after_move([0, 7, 8], [0, 6, 0], 1, 0, 10, 10)
    False
    """
    new_x = snake_xs[0] + dx
    new_y = snake_ys[0] + dy

    new_x = new_x % width
    new_y = new_y % height

    body_pairs = snake_as_pairs(snake_xs[1:], snake_ys[1:])
    return [new_x, new_y] in body_pairs


if __name__ == "__main__":
    import doctest
    doctest.testmod()
