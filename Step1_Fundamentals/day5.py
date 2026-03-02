def get_player_name():
    name = input("What is your name? ")
    return name

def ask_question(question,correct_answer):
    answer = input(question + " ")

    if answer.lower() == correct_answer.lower():
        print("Correct\n")
        return True
    else:
        print("Wrong\n")
        return False

def quiz_game():
    score =0

    questions =[
        ("What is 2**10?", "1024"),
        ("What is the capital of Andhra Pradesh?", "Amaravati"),
        ("What is discount on 1000 with 20% off?", "200"),
        ("How many continents are there?", "7"),
        ("What is the chemical symbol for water?", "H2O"),
    ]
    
    for question, answer in questions:
        if ask_question(question,answer):
            score +=1
    return score

def save_score(name,score):
    with open("scores.txt", "a") as file:
        file.write(f"{name} scored {score}/5\n")

def show_previous_scores():
    print("\n--- Previous Scores ---")
    try:
        with open("scores.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No Scores yet.")

def main():
    name = get_player_name()
    score = quiz_game()

    print(f"{name}, your final score is {score}/5")

    save_score(name,score)
    show_previous_scores()

main()
