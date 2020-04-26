# write your code here
from string import digits


def generate_row(row):
    return " ".join(row)


def print_board_game(matrix):

    line1 = generate_row(matrix[0])
    line2 = generate_row(matrix[1])
    line3 = generate_row(matrix[2])

    if not win(matrix, 'O') and not win(matrix, 'X'):
        line1 = line1.replace('_', ' ')
        line2 = line2.replace('_', ' ')
        line3 = line3.replace('_', ' ')

    print("""
    ---------
    | {0} |
    | {1} |
    | {2} |
    ---------
    """.format(line1, line2, line3))


def game_finished(matrix):
    if not valid_game_state(matrix):
        print('Impossible')
    elif win(matrix, 'O'):
        print('O wins')
    elif win(matrix, 'X'):
        print('X wins')
    elif not has_moves(matrix):
        print('Draw')


def generate_matrix(string):
    return [
        list(string[0:3]),
        list(string[3:6]),
        list(string[6:9])
    ]


def win(matrix, player):
    if is_horizontal_line(matrix, player):
        return True
    elif is_vertical_line(matrix, player):
        return True
    elif is_diagonal_line(matrix, player):
        return True
    else:
        return False


def is_horizontal_line(matrix, player):
    for row in matrix:
        if is_three_in_line(row, player):
            return True
    return False


def is_vertical_line(matrix, player):
    for column in range(3):
        column = [matrix[0][column], matrix[1][column], matrix[2][column]]
        if is_three_in_line(column, player):
            return True
    return False


def is_diagonal_line(matrix, player):
    length = len(matrix)
    diagonal_left_to_right = []
    diagonal_right_to_left = []

    for value in range(length):
        diagonal_left_to_right.append(matrix[value][value])
        diagonal_right_to_left.append(matrix[value][2-value])

    if is_three_in_line(diagonal_left_to_right, player) \
            or is_three_in_line(diagonal_right_to_left, player):
        return True

    return False


def is_three_in_line(group, player):
    unique_elements = set(group)
    return len(unique_elements) == 1 and player in unique_elements


def has_moves(matrix):
    elements = set([value for group in matrix for value in group])
    return "_" in elements


def valid_game_state(matrix):
    if win(matrix, 'O') and win(matrix, 'X'):
        return False

    total_o = len_element(matrix, 'O')
    total_x = len_element(matrix, 'X')
    diff = abs(total_x - total_o)

    return total_o == total_x or diff == 1


def len_element(matrix, element):
    return len([value for group in matrix for value in group if value == element])


def valid_raw_coordinates(raw_coordinates):
    words = raw_coordinates.split()
    for word in words:
        if word not in digits:
            print("You should enter numbers!")
            return False

        number = int(word)
        if not 1 <= number <= 3:
            print("Coordinates should be from 1 to 3!")
            return False

    return True


def play_player(matrix, raw_coordinates):
    if not valid_raw_coordinates(raw_coordinates):
        return False

    row, column = transform_coordinates(raw_coordinates)

    if matrix[row][column] != '_':
        print("This cell is occupied! Choose another one!")
        return False

    player = next_player(matrix)
    matrix[row][column] = player
    return True


def transform_coordinates(raw_coordinates):
    column, row = list(map(int, raw_coordinates.split()))
    return [3 - row, column - 1]


def next_player(matrix):
    total_o = len_element(matrix, 'O')
    total_x = len_element(matrix, 'X')
    return 'O' if total_o < total_x else 'X'


def finished(matrix):
    return not valid_game_state(matrix) or win(matrix, 'O') or win(matrix, 'X') or not has_moves(matrix)


def start():
    matrix = generate_matrix('_________')
    print_board_game(matrix)

    while True:
        raw_coordinates = input("Enter the coordinates: ")

        if not play_player(matrix, raw_coordinates):
            continue

        print_board_game(matrix)

        if finished(matrix):
            break

    game_finished(matrix)


start()
