def save_score(name,attempts):
    with open("game_scores.txt", "a") as file:
        if attempts:
            file.write(f"{name}: won in{attempts} attempts\n")
        else:
            file.write(f"{name}: lost the game\n")

def show_scores():
    print("\n--- Previous Game Results ---")
    try:
        with open("game_scores.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No previous scores found.")