import sys
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def summarize_git_status(status_file):
    # Read the content of the status file
    with open(status_file, 'r') as file:
        status_content = file.read()

    # Initialize Ollama LLM
    llm = Ollama(model="llama3.2:1b")

    # Create a prompt template with strict focus on brevity
    prompt = PromptTemplate(
        input_variables=["status"],
        template="""Analyze this Git status and provide exactly:

1. Changed files (max 1 line)
2. Next step (max 1 line)

Output format:
Changes: [list only file names]
Action: [single clear action]

Keep total response under 4 lines.
{status}"""
    )

    # Create an LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Generate the summary
    summary = chain.run(status=status_content)
    return summary.strip()

def analyze_files_for_staging(status_file):
    with open(status_file, 'r') as file:
        status_content = file.read()

    llm = Ollama(model="llama3.2")
    
    prompt = PromptTemplate(
        input_variables=["status"],
        template="""Analyze Git status and provide:

Stage these files:
[file names only, 1 line per file]

Skip these files:
[file names only that should be ignored]

Keep total response under 6 lines, no explanations.
{status}"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    
    try:
        analysis = chain.run(status=status_content)
        return analysis.strip()
    except Exception as e:
        return "Error: Could not analyze files."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llm.py <status_file>")
        sys.exit(1)

    status_file = sys.argv[1]
    
    if status_file == "status.txt":
        summary = summarize_git_status(status_file)
    elif status_file == "add_files_analysis.txt":
        summary = analyze_files_for_staging("status.txt")
    else:
        print(f"Unknown file: {status_file}")
        sys.exit(1)

    # Write the summary to response.txt
    with open("response.txt", "w") as file:
        file.write(summary)