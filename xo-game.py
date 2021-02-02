import os
import random
game_history = []


def Place(n):
    if n in game_history:
        return 'X'
    else:
        return n


def python_turn():
    python_choice = random.randint(1, 9)


for i in range(9):
    print('   '+str(Place(1))+'|'+str(Place(2))+'|'+str(Place(3)) +
          '\n  -------\n   '
          + str(Place(4))+'|' + str(Place(5))+'|'+str(Place(6)) +
          '\n  -------\n   '
          + str(Place(7))+'|'+str(Place(8))+'|'+str(Place(9)))
    python_turn()
    user_choice = int(input("You're turn: "))
    game_history.append(user_choice)
    os.system('cls' if os.name == 'nt' else 'clear')
