import requests

url = "http://localhost:11434/api/generate"

def ask_agent(question):

    data = {
        "model": "phi3:mini",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    return result.get("response", "No response from model")


while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = ask_agent(user)

    print("Agent:", reply)