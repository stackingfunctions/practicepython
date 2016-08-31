_DEBUG = False

def _debug(msg):
    if _DEBUG:
        print("[DEBUG] " + msg)

def check_rows_helper(matrix, player):
    """Checks if there is a winning row for player by running through a nested loop."""

    _debug("************")
    _debug("Checking rows for player " + str(player))

    for row in matrix:
        _debug("-----------")
        _debug("row: " + repr(row))

        player_wins = 1
        _debug("player_wins: " + str(player_wins))

        for col in row:
            _debug("col: " + repr(col))

            # This is not a winner because it is either not filled or it is filled by the other player
            if col != player:
                _debug("col != player - col:%d player:%d" % (col, player))

                player_wins = 0
                _debug("player_wins: " + str(player_wins))
                _debug("break")

                break

        # in case it's a winning row, return the winner
        if player_wins == 1:
            _debug("Player %d wins" % player)
            return player

    # No winner found
    _debug("Returning 0")
    return 0

def check_rows(matrix):
    """Check for winning rows for both players"""

    _debug("#########################")
    _debug("Checking rows " + repr(matrix))

    # Player 1 has a winning row
    if check_rows_helper(matrix, 1) == 1:
        return 1

    # Player 2 has a winning row
    elif check_rows_helper(matrix, 2):
        return 2

    # None of them have winning row
    else:
        return 0


def check_columns_helper(matrix, player):
    """Checks if there is a winning column for player by running through a nested loop,
    but referencing elements in column order ([ii][i])."""
    _debug("************")
    _debug("Checking columns for player " + repr(player))

    for i in list(range(len(matrix))):
        _debug("-----------")
        _debug("i: " + str(i))

        player_wins = 1
        _debug("player_wins = " + str(player_wins))

        for ii in list(range(len(matrix))):
            _debug("ii: " + str(ii))
            _debug("matrix[ii][i]: " + str(matrix[ii][i]))

            # This is not a winner because it is either not filled or it is filled by the other player
            if matrix[ii][i] != player:
                player_wins = 0
                _debug("player_wins = " + repr(player_wins))
                _debug("break")
                break

        # in case it's a winning row, return the winner
        if player_wins == 1:
            _debug("Player %d wins" % player)
            return player

    # No winner found
    _debug("Returning 0")
    return 0

def check_columns(matrix):
    _debug("#########################")
    _debug("Checking columns " + repr(matrix))

    # Player 1 has a winning column
    if check_columns_helper(matrix, 1) == 1:
        return 1

    # Player 2 has a winning column
    elif check_columns_helper(matrix, 2) == 2:
        return 2

    # None of them have winning column
    else:
        return 0



def check_decreasing_diagonal_helper(matrix, player):
    """Checking if there is a winning decreasing diagonal [(1,1), (2,2), (3,3), ...] for the player"""
    _debug("************")
    _debug("Checking decreasing diagonal for player " + repr(player))

    player_wins = 1
    for i in range(len(matrix)):
        _debug("-----------")
        _debug("i: " + str(i))
        _debug("matrix[i][i]: " + str(matrix[i][i]))

        # This is not a winner because it is either not filled or it is filled by the other player
        if matrix[i][i] != player:
            player_wins = 0
            _debug("player_wins = " + repr(player_wins))
            _debug("break")
            break

    # in case it's a winning row, return the winner
    if player_wins == 1:
        _debug("Player %d wins" % player)
        return player

    # No winner found
    _debug("Returning 0")
    return 0

def check_decreasing_diagonal(matrix):
    _debug("#########################")
    _debug("Checking decreasing diagonal for " + repr(matrix))

    # Player 1 has a winning decreasing diagonal
    if check_decreasing_diagonal_helper(matrix, 1) == 1:
        _debug("check_decreasing_diagonal() - returning 1")
        return 1

    # Player 2 has a winning decreasing diagonal
    elif check_decreasing_diagonal_helper(matrix, 2) == 2:
        _debug("check_decreasing_diagonal() - returning 2")
        return 2

    # None of them have winning decreasing diagonal
    else:
        _debug("check_decreasing_diagonal() - returning 0")
        return 0


def check_increasing_diagonal_helper(matrix, player):
    """Checking if there is a winning decreasing diagonal [(1,n-1), (2,n-2), (3,n-3), ...] for the player"""
    _debug("************")
    _debug("Checking decreasing diagonal for player " + repr(player))

    player_wins = 1
    _debug("player_wins = " + repr(player_wins))

    for i in range(len(matrix) - 1, -1, -1):
        _debug("-----------")
        _debug("i: " + str(i))
        _debug("matrix[i][i]: " + str(matrix[i][i]))

        for ii in range(len(matrix)):
            _debug("ii: " + str(ii))
            _debug("matrix[i][ii]: " + str(matrix[i][ii]))

            # This is not a winner because it is either not filled or it is filled by the other player
            if matrix[i][ii] != player:
                _debug("matrix[i][ii] != player - matrix[i][ii]: %d, player: %d" % (matrix[i][ii], player))
                player_wins = 0
                _debug("player_wins = " + repr(player_wins))
                _debug("break")
                break

        # in case it's a winning row, return the winner
        if player_wins == 1:
            _debug("Player %d wins" % player)
            return player

    # No winner found
    _debug("Returning 0")
    return 0


def check_increasing_diagonal(matrix):
    _debug("************")
    _debug("Checking increasing diagonal for " + repr(matrix))

    # Player 1 has a winning increasing diagonal
    if check_increasing_diagonal_helper(matrix, 1) == 1:
        return 1

    # Player 2 has a winning increasing diagonal
    elif check_increasing_diagonal_helper(matrix, 2) == 2:
        return 2

    # None of them have winning decreasing diagonal
    else:
        return 0


def check_diagonals(matrix):
    """There are two diagonals. If the first one is a winner for someone, return the player, otherwise check the other diagonal"""
    result = check_decreasing_diagonal(matrix)
    if result == 0:
        result = check_increasing_diagonal(matrix)

    return result


def check_winner(matrix):
    """Check the winner by checking rows, columns, and diagonals until a winner is found."""
    result = check_rows(matrix)
    _debug("check_columns(matrix) returned: " + str(result))

    # Was there a winner in the rows?
    if result != 0:
        return result

    result = check_columns(matrix)
    _debug("check_columns(matrix) returned: " + str(result))

    # Was there a winner in the columns?
    if result != 0:
        return result

    result = check_diagonals(matrix)
    _debug("check_columns(matrix) returned: " + str(result))

    # Was there a winner in the diagonals?
    if result != 0:
        return result

    # Noone wins
    return 0

def print_result(winner, matrix):
    """Simply convert the integer representation of the winner to a printable name and print the matrix"""
    _debug("print_result - winner: %d" % winner + " matrix: " + repr(matrix))
    winner_name = "noone"
    if winner == 1:
        winner_name = "Player1"
    if winner == 2:
        winner_name = "Player2"

    print("The winner is %s for " % winner_name + repr(matrix))


if __name__ == "__main__":

    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
    print("\n\nExpected: Player 2")
    print_result(check_winner(winner_is_2), winner_is_2)

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
    print("\n\nExpected: Player 1")
    print_result(check_winner(winner_is_1), winner_is_1)

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]
    print("\n\nExpected: Player 1")
    print_result(check_winner(winner_is_also_1), winner_is_also_1)

    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]
    print("\n\nExpected: noone")
    print_result(check_winner(no_winner), no_winner)

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]
    print("\n\nExpected: noone")
    print_result(check_winner(also_no_winner), also_no_winner)
