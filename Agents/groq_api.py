import os
from groq import Groq

client = Groq(
        api_key=os.getenv('GROQ_API_KEY')
)

roles = {

    "assistant":
    """
    You are a helpful AI assistant.
    Answer clearly and briefly.
    """,

    "mentor":
    """
    You are a friendly mentor.
    Explain concepts simply with examples.
    """,

    "researcher":
    """
    You are a research assistant.
    Provide detailed explanations.
    """,

    "coding":
    """
    You are a senior Python engineer.
    Write clean Python code and explain it.
    """,

    "planner":
    """
    You are a productivity planner.
    Create clear step-by-step plans.
    """
}


def ask_groq(question, role="assistant"):

    system_prompt = roles.get(role, roles["assistant"])

    try:

        chat = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )

        return chat.choices[0].message.content

    except Exception:

        return "Cloud AI unavailable."
    