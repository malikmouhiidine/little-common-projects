import os
import random
game_history = {}


def Place(n):
    if n in game_history:
        return str(game_history[n])
    else:
        return str(n)


def python_turn():
    python_choice = random.randint(1, 9)
    if not python_choice in game_history:
        game_history[python_choice] = 'O'
    else:
        python_turn()


for turn in range(4):
    print('Round: ' + str(turn+1))
    # print(game_history)  # debug print statement
    print('   '+Place(1)+'|'+Place(2)+'|'+Place(3) +
          '\n  -------\n   '
          + Place(4)+'|' + Place(5)+'|'+Place(6) +
          '\n  -------\n   '
          + Place(7)+'|'+Place(8)+'|'+Place(9))
    user_choice = int(input("You're turn: "))
    if user_choice not in game_history:
        game_history[user_choice] = 'X'
    else:
        print('\nplease make sure to print the right value\n')
        exit()
    python_turn()
    os.system('cls' if os.name == 'nt' else 'clear')
