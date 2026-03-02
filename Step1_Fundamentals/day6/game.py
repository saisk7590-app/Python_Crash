import random
from utils import choose_difficulty

def play_game():
    max_num,max_attempts = choose_difficulty()
    secret = random.randint(1, max_num)

    print(f"\nI'm thinking of a number between 1 and {max_num}. You have {max_attempts} attempts.")
    print(f"Yoy get {max_attempts} tries.\n")

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess (attempt {attempts+1}/{max_attempts}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1

        if guess == secret:
            print(f"🎉 You guessed it in {attempts} tries!")
            return attempts

        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"\n❌ No more tries! The number was {secret}.")
    return None
