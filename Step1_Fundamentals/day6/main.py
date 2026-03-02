from game import play_game
from file_manager import save_score, show_scores

def main():
    print("🎮 Welcome to the Ultimate Guessing Game")
    name = input("Enter your name: ")

    while True:
        attempts = play_game()
        save_score(name, attempts)

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            break

    show_scores()
    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()