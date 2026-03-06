from datetime import datetime
import requests

def get_today_date():

    today = datetime.now()

    return today.strftime("Today is %d %B %Y")


def get_location():

    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        city = data["city"]
        country = data["country"]

        return f"You are likely in {city}, {country}"

    except:
        return "Location detection failed."