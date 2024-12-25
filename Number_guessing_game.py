import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("enter a number between 1 and 100: "))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('You guess the right number...Congratulations')
            break
    except ValueError:
        print("Enter a valid Number!")