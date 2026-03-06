import requests

url = "http://localhost:11434/api/generate"


def ask_llm(prompt):

    data = {
        "model": "phi3:mini",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=30)

    result = response.json()

    return result["response"]