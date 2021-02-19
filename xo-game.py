import os
from time import sleep
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


def best_move(board):
    available_spots = (
        available_spot for available_spot in range(0, 9) if available_spot not in board)
    best_score = -float('inf')
    for available_spot in available_spots:
        board[available_spot] = 'O'
        score = minimax(board, 0, False)
        if score > best_score:
            best_score = score
            move = available_spot
        del board[available_spot]
    return move


def minimax(board, depth, is_maximazer_turn):
    if Win('O', board):
        return 1
    elif Win('X', board):
        return -1
    if len(board) == 9 and not Win('O', board) and not Win('X', board):
        return 0
    if is_maximazer_turn:
        available_spots = (
            available_spot for available_spot in range(0, 9) if available_spot not in board)
        best_score = -float('inf')
        for available_spot in available_spots:
            board[available_spot] = 'O'
            score = minimax(board, depth+1, False)
            best_score = max(score, best_score)
            del board[available_spot]
        return best_score
    else:
        available_spots = (
            available_spot for available_spot in range(0, 9) if available_spot not in board)
        best_score = float('inf')
        for available_spot in available_spots:
            board[available_spot] = 'X'
            score = minimax(board, depth+1, True)
            best_score = min(score, best_score)
            del board[available_spot]
        return best_score


def python_turn(turn):
    board = game_history.copy()
    game_history[best_move(board)] = 'O'


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


def Win(n, game_history=game_history):
    if len(game_history) == 1:
        return False
    for k, v in game_history.items():
        n_places_dict.setdefault(v, []).append(k)
    for i in winning_combination:
        if all(elem in n_places_dict[n] for elem in i):
            n_places_dict.clear()
            return True
    n_places_dict.clear()
    return False


def table():
    print('   '+Place(0)+'|'+Place(1)+'|'+Place(2) +
          '\n  -------\n   '
          + Place(3)+'|' + Place(4)+'|'+Place(5) +
          '\n  -------\n   '
          + Place(6)+'|'+Place(7)+'|'+Place(8))


for turn in range(5):
    print('Round: ' + str(turn+1))
    python_turn(turn)
    check_win()
    print(game_history)  # debugging print statement
    table()
    if turn != 4:
        user_choice = int(input("You're turn: "))
        if user_choice not in game_history and user_choice >= 0 and user_choice <= 8:
            game_history[user_choice] = 'X'
        else:
            print('\nplease make sure to print the right value\n')
            exit()
    os.system('cls' if os.name == 'nt' else 'clear')
    check_win()

print('\nNo one wins!\n')
exit()
