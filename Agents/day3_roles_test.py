import requests

url = "http://localhost:11434/api/chat"

def ask_llm(system_role, user_question):

    data = {
        "model": "phi3:mini",
        "messages": [
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_question}
        ],
        "stream": False
    }

    response = requests.post(url, json=data)

    return response.json()["message"]["content"]


# System roles
friendly_role = "You are a friendly mentor who explains things simply and supportively."

teacher_role = "You are a strict coding teacher. Give precise and formal explanations."


while True:

    question = input("\nAsk a question (type exit to stop): ")

    if question.lower() == "exit":
        break

    print("\n--- Friendly Mentor Answer ---\n")
    print(ask_llm(friendly_role, question))

    print("\n--- Strict Teacher Answer ---\n")
    print(ask_llm(teacher_role, question))