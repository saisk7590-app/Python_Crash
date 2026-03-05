def calculate(expression):

    try:
        result = eval(expression)
        return f"Answer: {result}"

    except:
        return "Invalid math expression."