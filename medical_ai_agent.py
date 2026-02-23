import os
import sys
import re
from pypdf import PdfReader
from langchain_ollama import ChatOllama

# Set encoding for Windows console to handle emojis
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

llm = ChatOllama(model="phi3")

# Tools definition
def read_pdf_tool(filename: str):
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    filepath = os.path.join("Reports", filename)
    if not os.path.exists(filepath):
        return f"File not found in Reports directory. Looked for {filepath}"
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def read_all_reports_tool(_=None):
    combined_text = ""
    reports_dir = "Reports"
    if not os.path.exists(reports_dir):
        return "Reports directory not found."
    for file in os.listdir(reports_dir):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(reports_dir, file))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    combined_text += page_text + "\n"
    return combined_text if combined_text else "No reports found in Reports folder."

tools = {
    "ReadPDF": read_pdf_tool,
    "ReadAllReports": read_all_reports_tool
}

agent_prompt = """You are a medical assistant having a conversation with a human.
You have access to the following tools:
- ReadPDF: Read a specific patient report PDF file. Input should be the filename.
- ReadAllReports: Read all patient report PDFs in folder. Input can be anything.

Use the following format:
Thought: you should always think about what to do
Action: the action to take, should be one of [ReadPDF, ReadAllReports]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Human: {input}
{agent_scratchpad}"""

print("🧠 Medical Agent Ready")

while True:
    try:
        query = input("\nAsk your medical question (or type exit): ")
    except EOFError:
        break

    if query.lower() == "exit":
        break

    scratchpad = ""
    while True:
        prompt = agent_prompt.format(input=query, agent_scratchpad=scratchpad)
        response = llm.invoke(prompt).content
        
        print(f"\n[Agent Thought Process]:\n{response}\n")

        if "Final Answer:" in response:
            final_answer = response.split("Final Answer:")[-1].strip()
            print("\n🩺 Agent Response:\n")
            print(final_answer)
            break
            
        action_match = re.search(r"Action: ([\w]+)", response)
        action_input_match = re.search(r"Action Input: (.*)", response)
        
        if action_match and action_input_match:
            action = action_match.group(1).strip()
            action_input = action_input_match.group(1).strip()
            
            if action in tools:
                print(f"🛠️ Using Tool '{action}' with input '{action_input}'...")
                observation = tools[action](action_input)
                # Keep scratchpad concise to avoid token limits
                if len(observation) > 1000:
                    observation = observation[:1000] + "... [TRUNCATED]"
                scratchpad += f"{response}\nObservation: {observation}\n"
            else:
                scratchpad += f"{response}\nObservation: Tool {action} not found.\n"
        else:
            # Fallback if the model didn't format correctly
            print("\n🩺 Agent Response (Fallback):\n")
            print(response)
            break