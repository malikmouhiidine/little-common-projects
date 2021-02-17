import os
import time
game_history = {}
winning_combination = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
n_places_dict = {}


def Place(n):
    if n in game_history:
        return str(game_history[n])
    return str(n)


def minimax(board, player):
    # loop from 0 to 9 excluding what's already in the board
    available_spots = (
        available_spot for available_spot in range(0, 9) if available_spot not in board)
    if Win('X'):
        return {'score': -1}
    elif Win('O'):
        return {'score': 1}
    if len(board) == 9:
        return {'score': 0}
    moves = []
    for available_spot in available_spots:
        move = {}
        board[available_spot] = player
        move['index'] = available_spot
        if player == 'O':
            result = minimax(board, 'X')
            move['score'] = result['score']
        else:
            result = minimax(board, 'O')
            move['score'] = result['score']

        moves.append(move)
        if player == 'O':
            best_score = -float('inf')
            for i in range(len(moves)):
                if moves[i]['score'] > best_score:
                    best_move = i
        else:
            best_score = float('inf')
            for i in range(len(moves)):
                if moves[i]['score'] < best_score:
                    best_move = i
    return moves[best_move]


def python_turn(turn):
    if turn == 0:
        if not 4 in game_history:
            game_history[4] = 'O'
        else:
            game_history[2] = 'O'
    else:
        board = game_history.copy()
        game_history[minimax(board, 'O')['index']] = 'O'


def check_win():
    if Win('X'):
        table()
        print('\nYou win!\n')
        exit()
    elif Win('O'):
        table()
        print('\nYou lose!\n')
        exit()
    return True


def Win(n):
    for k, v in game_history.items():
        n_places_dict.setdefault(v, []).append(k)
    for i in winning_combination:
        if all(elem in n_places_dict[n] for elem in i):
            return True
    return False


def table():
    print('   '+Place(0)+'|'+Place(1)+'|'+Place(2) +
          '\n  -------\n   '
          + Place(3)+'|' + Place(4)+'|'+Place(5) +
          '\n  -------\n   '
          + Place(6)+'|'+Place(7)+'|'+Place(8))


for turn in range(5):
    print('Round: ' + str(turn+1))
    print(game_history)  # debugging print statement
    table()
    user_choice = int(input("You're turn: "))
    if user_choice not in game_history:
        game_history[user_choice] = 'X'
    else:
        print('\nplease make sure to print the right value\n')
        exit()
    if turn != 4:
        python_turn(turn)
    os.system('cls' if os.name == 'nt' else 'clear')
    check_win()

print('\nNo one wins!\n')
exit()
