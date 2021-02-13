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


def dumb_move(last_player_move):
    for i in range(9):
        if not last_player_move - (i + 1) < 0 and not last_player_move - (i + 1) in game_history:
            game_history[last_player_move - (i + 1)] = 'O'
            return True
        elif not last_player_move + (i + 1) > 8 and not last_player_move + (i + 1) in game_history:
            game_history[last_player_move + (i + 1)] = 'O'
            return True
    return False


def minimax(depth, board, is_maximizing_player_turn):
    # loop from 0 to 9 excluding what's already in the board
    gen = (i for i in range(0, 9) if i not in board)
    if len(board) == 9:
        if Win('X'):
            value = 1
        elif Win('O'):
            value = -1
        else:
            value = 0
        return value
    if is_maximizing_player_turn:
        best_val = -float('inf')
        for i in gen:
            value = minimax(depth+1, board, False)
            best_val = max(best_val, value)
        return best_val
    else:
        best_val = float('inf')
        for i in gen:
            value = minimax(depth+1, board, True)
            best_val = min(best_val, value)
        return best_val


def python_turn(turn):
    game_history_aslist = list(game_history.items())
    last_player_move = game_history_aslist[-1][0]
    if turn == 0:
        if not 4 in game_history:
            game_history[4] = 'O'
        else:
            game_history[2] = 'O'
    else:
        # dumb_move(last_player_move)
        minimax(0, game_history, True)


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
