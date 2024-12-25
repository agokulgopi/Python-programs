import random

choices = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
while True:
    user_choice = input('Enter a choice ? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid Choice!')

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
            print('You win')
    else:
        print('You lose!')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break