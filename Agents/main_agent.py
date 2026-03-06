from llm_api import ask_llm
from groq_api import ask_groq

from tools.calculator import calculate
from tools.file_organizer import organize_folder
from tools.system_tools import get_today_date, get_location
from tools.weather_tool import get_weather


# -----------------------------
# TASK DETECTION
# -----------------------------

def detect_tasks(user):

    user = user.lower()
    tasks = []

    if "date" in user or "today" in user:
        tasks.append("date")

    if "location" in user or "where am i" in user:
        tasks.append("location")

    if "weather" in user:
        tasks.append("weather")

    if any(op in user for op in ["+", "-", "*", "/", "**"]):
        tasks.append("calculator")

    if "organize" in user or "clean folder" in user:
        tasks.append("organize")

    if "python" in user or "code" in user or "program" in user:
        tasks.append("coding")

    if "research" in user or "detail" in user or "explain deeply" in user:
        tasks.append("researcher")

    if "explain" in user and "deeply" not in user:
        tasks.append("mentor")

    if "plan" in user or "schedule" in user:
        tasks.append("planner")

    if not tasks:
        tasks.append("chat")

    return tasks

# -----------------------------
# AGENT LOOP
# -----------------------------

print("\n🤖 AI Agent Ready\n")

while True:

    try:
        user = input("You: ")
    except EOFError:
        break

    if user.lower() in ["exit", "stop"]:
        print("Agent shutting down...")
        break

    tasks = detect_tasks(user)
    results = []

    for task in tasks:

        try:

            # DATE
            if task == "date":
                results.append(get_today_date())

            # LOCATION
            elif task == "location":
                results.append(get_location())

            # WEATHER
            elif task == "weather":

                import re
                match = re.search(r'weather(?:\s+in)?\s+(\w+)', user, re.IGNORECASE)
                if match:
                    city = match.group(1)
                else:
                    city = ""

                if city == "":
                    city = input("Enter city: ")

                results.append(get_weather(city))
            # CALCULATOR
            elif task == "calculator":
                results.append(calculate(user))

            # FILE ORGANIZER
            elif task == "organize":

                path = input("Enter folder path: ")

                if path.lower() == "exit":
                    results.append("File organization cancelled.")
                else:
                    results.append(organize_folder(path))

            # CODING TASKS
            elif task == "coding":
                results.append(ask_groq(user, role="coding"))

            # RESEARCH
            elif task == "researcher":
                results.append(ask_groq(user, role="researcher"))

            # PLANNER
            elif task == "planner":
                results.append(ask_groq(user, role="planner"))

            # GENERAL CHAT
            else:
                try:
                    results.append(ask_llm(user))
                except:
                    results.append(ask_groq(user, role="assistant"))

        except Exception as e:
            results.append(f"Error: {str(e)}")

    print("\nAgent:\n")

    for r in results:
        print(r)
        print()