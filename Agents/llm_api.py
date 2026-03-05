import requests

url = "http://localhost:11434/api/generate"

def ask_llm(question):

    data = {
        "model": "phi3:mini",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    return response.json()["response"]