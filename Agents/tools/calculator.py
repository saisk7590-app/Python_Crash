import re

def calculate(expression):

    try:
        expr = re.findall(r"[0-9\.\+\-\*\/\(\)]+", expression)
        expr = "".join(expr)

        result = eval(expr)

        return f"Result: {result}"

    except:
        return "Could not calculate."