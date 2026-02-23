import os
from pypdf import PdfReader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Load local Ollama model (make sure ollama is running)
llm = OllamaLLM(model="phi3")

# Function to read a single PDF file
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Improved Medical Prompt
template = """
You are a senior medical consultant.

Based ONLY on the following medical report, provide:

1. Diagnosis
2. Condition severity (Mild / Moderate / Severe)
3. Risk level (Low / Moderate / High)
4. Immediate medical concerns (if any)
5. Recommended lifestyle changes
6. Whether urgent doctor visit is required

Medical Report:
{report_data}

User Question:
{question}

Provide a clear and structured answer.
"""

prompt = ChatPromptTemplate.from_template(template)

print("📂 Medical AI Assistant Ready")

while True:
    filename = input("\nEnter report file name (or type exit): ")

    if filename.lower() == "exit":
        print("Exiting Medical AI...")
        break

    # Automatically add .pdf if user forgot
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    # Check if file exists in current project folder
    if not os.path.exists(filename):
        print("❌ Report not found in project folder. Try again.")
        continue

    print("📖 Reading report...")

    report_text = read_pdf(filename)

    question = input("Ask question about this report: ")

    final_prompt = prompt.format(
        report_data=report_text,
        question=question
    )

    print("\n🩺 Doctor AI:\n")

    response = llm.invoke(final_prompt)

    print(response)
    print("\n----------------------------")