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
password_generated = ''.join(list_of_chosen_chars)
print(password_generated)
asking_if_user_want_save_password = input(
    'Do you want to download password to your downloads directory (Y, N): ')
if (('y' in asking_if_user_want_save_password.lower())):
    pass
