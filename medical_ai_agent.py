import os
from pypdf import PdfReader
from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, Tool, AgentType

llm = OllamaLLM(model="phi3")

# Tool 1
def read_pdf_tool(filename):
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    if not os.path.exists(filename):
        return "File not found."

    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

# Tool 2
def read_all_reports(_):
    combined_text = ""
    for file in os.listdir():
        if file.endswith(".pdf"):
            reader = PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    combined_text += page_text + "\n"

    return combined_text if combined_text else "No reports found."

tools = [
    Tool(
        name="ReadPDF",
        func=read_pdf_tool,
        description="Read a specific patient report PDF file."
    ),
    Tool(
        name="ReadAllReports",
        func=read_all_reports,
        description="Read all patient report PDFs in folder."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("🧠 Medical Agent Ready")

while True:
    query = input("\nAsk your medical question (or type exit): ")

    if query.lower() == "exit":
        break

    response = agent.run(query)

    print("\n🩺 Agent Response:\n")
    print(response)