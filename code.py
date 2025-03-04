import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Correct! You guessed it.")
else:
    print(f"Wrong! The number was {number}")
