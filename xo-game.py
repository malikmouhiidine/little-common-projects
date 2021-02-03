import os
import random
game_history = {}


def Place(n):
    if n in game_history:
        return str(game_history[n])
    return str(n)


def python_turn():
    python_choice = random.randint(0, 8)
    game_history[python_choice] = 'O' if not python_choice in game_history else python_turn()


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
    n_places_dict = {}
    for k, v in game_history.items():
        n_places_dict.setdefault(v, []).append(k)
    # print(n_places_dict[n])  # debugging print statement
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
    for i in winning_combination:
        # print(i)  # debugging print statement
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
    # print(game_history)  # debugging print statement
    table()
    user_choice = int(input("You're turn: "))
    if user_choice not in game_history:
        game_history[user_choice] = 'X'
    else:
        print('\nplease make sure to print the right value\n')
        exit()
    if turn != 4:
        python_turn()
    os.system('cls' if os.name == 'nt' else 'clear')
    check_win()

print('\nNo one wins!\n')
exit()
