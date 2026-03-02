def choose_difficulty():
    print("Choose a difficulty level: easy, medium, hard")
    level = input("Type here: ").strip().lower()

    if level == "easy":
        return 50,10
    elif level == "hard":
        return 200,5
    else:
        return 200,7
    