from llm_api import ask_llm
from tools.calculator import calculate
from tools.file_organizer import organize_folder


while True:

    user = input("You: ")

    if user.lower() == "exit":
        break


    # math detection
    if any(op in user for op in ["+", "-", "*", "/", "**"]):

        reply = calculate(user)

    # folder organization
    elif "organize" in user.lower():

        path = input("Enter folder path: ")
        reply = organize_folder(path)

    # normal LLM question
    else:

        reply = ask_llm(user)


    print("Agent:", reply)