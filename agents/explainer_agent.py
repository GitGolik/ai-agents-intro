from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import FunctionTool

from tools.file_writer import save_markdown_file

MODEL_NAME = "qwen2.5-coder:1.5b"

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model=f"ollama_chat/{MODEL_NAME}"),
    description="Explains programming topics and saves the explanation as Markdown.",
    instruction="""
You are a programming teacher for beginner students.

First, explain the topic provided by the user.

Then, use the save_markdown_file tool to save the explanation.

Use this file path:
output/explainer_output.md

Your Markdown content must contain exactly these sections:

## Explanation
A short explanation of 2 to 4 sentences.

## Key concepts
A bullet list of 3 to 5 key concepts.

## Example
One simple code example with a brief explanation.

After saving the file, tell the user the file has been saved.
""",
    tools=[FunctionTool(save_markdown_file)],
)
