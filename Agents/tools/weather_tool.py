import requests

def get_weather(city):

    city = city.strip()

    url = f"https://wttr.in/{city}?format=3"

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200 and response.text.strip() != "":
            return response.text.strip()

        else:
            return "Weather service unavailable."

    except requests.exceptions.RequestException:
        return "Weather data not available."