import re

from llm_api import ask_llm
from groq_api import ask_groq

from tools.calculator import calculate
from tools.file_organizer import organize_folder
from tools.system_tools import get_today_date, get_location
from tools.weather_tool import get_weather

from templates.template_engine import detect_template, fill_template


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
# FORMAT DETECTION (Day 4)
# -----------------------------

def detect_format(user):

    user = user.lower()

    if "bullet" in user:
        return "bullet"

    if "table" in user:
        return "table"

    if "json" in user:
        return "json"

    return "normal"


def detect_strict_mode(user):

    user = user.lower()

    if "only" in user or "strict" in user:
        return True

    return False


# -----------------------------
# PROMPT BUILDER
# -----------------------------

def build_prompt(user, format_type, strict):

    instruction = "Answer the user's request clearly."

    if format_type == "bullet":
        output_format = "Return the answer as bullet points."

    elif format_type == "table":
        output_format = "Return the answer in a markdown table."

    elif format_type == "json":
        output_format = "Return the answer as JSON."

    else:
        output_format = "Return a normal explanation."

    rules = ""

    if strict:
        rules = "IMPORTANT: Return ONLY the requested structure. No extra text."

    prompt = f"""
Instruction:
{instruction}

User Request:
{user}

Output Format:
{output_format}

Rules:
{rules}
"""

    return prompt


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

    # -----------------------------
    # TEMPLATE ENGINE (Day 5)
    # -----------------------------

    template_name = detect_template(user)

    if template_name:
        templated_prompt = fill_template(template_name, user)
    else:
        templated_prompt = user

    # Apply formatting rules (Day 4)
    format_type = detect_format(user)
    strict_mode = detect_strict_mode(user)

    prompt = build_prompt(templated_prompt, format_type, strict_mode)

    # -----------------------------
    # TASK EXECUTION
    # -----------------------------

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

                match = re.search(r'weather(?:\s+in)?\s+(\w+)', user, re.IGNORECASE)

                if match:
                    city = match.group(1)
                else:
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

            # CODING ROLE
            elif task == "coding":
                results.append(ask_groq(prompt, role="coding"))

            # RESEARCH ROLE
            elif task == "researcher":
                results.append(ask_groq(prompt, role="researcher"))

            # MENTOR ROLE
            elif task == "mentor":
                results.append(ask_groq(prompt, role="mentor"))

            # PLANNER ROLE
            elif task == "planner":
                results.append(ask_groq(prompt, role="planner"))

            # CHAT / FALLBACK
            else:

                try:
                    results.append(ask_llm(prompt))
                except:
                    results.append(ask_groq(prompt, role="assistant"))

        except Exception as e:
            results.append(f"Error: {str(e)}")

    print("\nAgent:\n")

    for r in results:
        print(r)
        print()