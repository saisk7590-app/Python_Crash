import random

def play_game():
    # Choose difficulty
    print("Choose difficulty: easy, medium, hard")
    level = input("Type here: ").strip().lower()

    if level=="easy":
        max_num = 50
        max_attempts = 10
    elif level =="hard":
        max_num = 200
        max_attempts = 5
    else: #medium level
        max_num =100
        max_attempts=7

    secret = random.randint(1, max_num)
    print(f"\nI'm thinking of a number between 1 and {max_num}. You get {max_attempts} tries.")

    attempts = 0

    while attempts < max_attempts:
        guess = int(input(f"Guess (attempt {attempts+1}/{max_attempts}): "))
        attempts += 1

        if guess == secret:
            print(f"🎉 You guessed it in {attempts} tries!")
            break

        # Too high / too low
        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        # Warmth hint
        diff = abs(guess-secret)
        if diff <= max_num * 0.1:
            print("🔥 You're warm!")
        elif diff <= max_num * 0.25:
            print("🙂 You're getting closer!")
        else:
            print("❄️ You're cold!")
    else:
        print(f"\n❌ No more tries! The number was {secret}.")

# Main loop to replay
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye.")
        break
        