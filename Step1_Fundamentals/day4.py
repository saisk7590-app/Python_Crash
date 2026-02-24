def get_player_info(name):
    name = input("Enter your name: ")
    return name

def ask_quetions(question,correct_answer):
    answer = input(question +" ")
    
    if answer.lower() == "quit":
        return "quit"
    
    if answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print("wrong!\n")
        return False

def quiz_game():
    score =0

    questions = [
         ("What is the capital of France?", "Paris"),
         ("What is 2 + 2?", "4"),
         ("What is the largest mammal?", "Blue Whale")
    ]

    for question,answer in questions:
        result = ask_quetions(question,answer)

        if result == "quit":
            print ("you chose to quit the game.")
            break

        if result:
            score +=1
    
    print("Your final score is:", score)

def main():
    name = get_player_info("name")
    print("\nWelcome", name + "!")
    print("Type 'quit' anytime to stop.\n")

    quiz_game()


main()


