import random

print("🎲 Welcome to the Number Guessing Game!")

secret = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 20: ")
    
    # Convert to number
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a number, not text.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"✅ Correct! The number was {secret}. You guessed it in {attempts} tries.")
        break
