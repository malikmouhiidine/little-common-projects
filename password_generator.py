import random

how_much_char_user_wants = input(
    'how many characters you want\'s in your password: ')
try:
    how_much_char_user_wants = int(how_much_char_user_wants)
except Exception:
    print('please enter a valid number')
    exit()

list_of_chosen_chars = []
for i in range(how_much_char_user_wants):
    list_of_chosen_chars.append(random.choice(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'))
print(''.join(list_of_chosen_chars))
