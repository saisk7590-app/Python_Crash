# templates/prompt_templates.py

TEMPLATES = {

    "explanation": """
Explain {topic} in 3 bullet points.
""",

    "json_explanation": """
Explain {topic} in JSON format with keys:
definition, example, use_case.

Return ONLY JSON.
""",

    "comparison": """
Compare {item1} and {item2} in a table format.
""",

    "step_guide": """
Give step-by-step instructions to learn {skill}.
Limit to 5 steps.
""",

    "summary": """
Summarize the following text in 5 bullet points:

{text}
"""
}