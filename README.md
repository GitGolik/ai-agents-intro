# AI Agents in Python

## Description

This project creates a beginner-friendly Markdown study guide for a programming topic.

The workflow uses three AI agents:

1. The **Explainer Agent** explains the topic.
2. The **Practice Designer Agent** creates a short practice exercise based on the explanation.
3. The **Reviewer Agent** reviews the draft and gives short, actionable feedback.

The project then validates that the required Markdown sections are present and saves the final study guide in the `output/` directory.

## Requirements

- Python 3.10 or newer
- Ollama installed and running locally
- A local Ollama model installed
- A Python virtual environment

The project was tested with:

```text
Python 3.14
Ollama
qwen2.5-coder:1.5b
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install google-adk litellm python-dotenv httpx mcp
```

Make sure Ollama is running:

```bash
ollama serve
```

Check that your model is available:

```bash
ollama list
```

If the model is not installed, download it:

```bash
ollama pull qwen2.5-coder:1.5b
```

## Configuration

Create a `.env` file from the example file:

```bash
cp .env.example .env
```

Then set the following values:

```env
OLLAMA_API_BASE=http://localhost:11434
OLLAMA_MODEL=qwen2.5-coder:1.5b
```

- `OLLAMA_API_BASE` is the address of the local Ollama server.
- `OLLAMA_MODEL` is the exact name of an Ollama model installed on your machine.

Do not commit the `.env` file. It is excluded by `.gitignore`.

## How to Run

From the project root, with the virtual environment activated:

```bash
python3 main.py "Python decorators"
```

You can also test other topics:

```bash
python3 main.py "Python list comprehensions"
python3 main.py "HTTP status codes"
```

The program will:

1. Check that the topic is not empty.
2. Check that Ollama is running.
3. Check that the selected model is available.
4. Run the Explainer Agent.
5. Run the Practice Designer Agent.
6. Run the Reviewer Agent.
7. Validate the required Markdown sections.
8. Save the final guide to `output/study_guide.md`.

## Example Input

```bash
python3 main.py "Python decorators"
```

## Example Output

```markdown
# Python decorators

## Topic
Python decorators are a way to modify the behavior of a function.

## Simple Explanation
A decorator is a function that wraps another function. It can add behavior
before or after the original function runs.

## Key Concepts
- Functions
- Higher-order functions
- The `@decorator` syntax
- Wrapper functions

## Example
```python
def say_hello():
    print("Hello!")

say_hello()
```

## Practice Exercise
Write a function that prints a greeting message.

## Common Mistakes
- Forgetting to call the function.
- Confusing a function definition with a function call.

## Review Comments
The explanation is clear, but the example could show a decorator explicitly.

## Final Summary
Decorators help reuse behavior without rewriting a function.
```

The exact wording and structure may vary because the project uses a local model.

## Project Structure

```text
.
├── agents/
│   ├── explainer_agent.py
│   ├── practice_designer_agent.py
│   └── reviewer_agent.py
├── tools/
│   ├── file_writer.py
│   └── validation.py
├── output/
│   └── study_guide.md
├── config.py
├── main.py
├── .env
├── .env.example
└── README.md
```

## Agents

### Explainer Agent

The Explainer Agent receives a programming topic and creates the main study guide.

It produces:

- Topic
- Simple explanation
- Key concepts
- Example
- Practice exercise
- Common mistakes
- Review comments
- Final summary

### Practice Designer Agent

The Practice Designer Agent receives the original topic and the explanation created by the Explainer Agent.

It creates:

- One small practice exercise
- Expected input, when relevant
- Expected output, when relevant
- One or two hints

It does not rewrite the explanation.

### Reviewer Agent

The Reviewer Agent receives the draft study guide and reviews it.

It identifies:

- Missing information
- Unclear explanations
- Possible improvements

It gives a short approval or revision recommendation. It does not replace the other agents or create a completely new guide.

## Tools

### `save_markdown_file()`

This tool saves Markdown content to a file.

It:

- Creates the `output/` directory if needed.
- Writes the Markdown content to disk.
- Returns a success message or a readable error message.

### `validate_required_sections()`

This tool checks that the final Markdown contains the required sections:

- Topic
- Simple Explanation
- Key Concepts
- Example
- Practice Exercise
- Common Mistakes
- Review Comments
- Final Summary

It returns whether the guide is valid and which sections are missing.

## Self-Validation Checklist

- [x] I created `agents/explainer_agent.py`.
- [x] I created `agents/practice_designer_agent.py`.
- [x] I created `agents/reviewer_agent.py`.
- [x] I created `tools/file_writer.py`.
- [x] I created `tools/validation.py`.
- [x] The Explainer Agent receives a topic.
- [x] The Practice Designer Agent receives the previous explanation.
- [x] The Reviewer Agent receives the draft study guide.
- [x] The workflow runs in a sequential order.
- [x] The final Markdown contains the required sections.
- [x] The validation tool checks the required sections.
- [x] The Markdown file is saved in `output/study_guide.md`.
- [x] The README explains how to run the project.

## Reflection

### Direct LLM call versus AI agent

A direct LLM call sends one prompt to a model and returns text. It is useful for a single, isolated task.

An AI agent has a role, instructions, and optionally tools. It can follow a defined workflow, use previous results, and perform actions through tools. In this project, each agent has a specific responsibility instead of trying to do everything at once.

### Role of each agent

- The **Explainer Agent** creates the initial explanation and study guide.
- The **Practice Designer Agent** turns the explanation into a practical beginner exercise.
- The **Reviewer Agent** checks the draft for missing information, unclear explanations, and possible improvements.

### Role of each tool

- `save_markdown_file()` performs a deterministic action: it writes Markdown content to a file.
- `validate_required_sections()` performs a deterministic check: it verifies that all required Markdown headings are present.

The LLM generates flexible content, while the tools provide predictable behavior.

### Most difficult part

The most difficult part was making the local model follow the exact Markdown structure. The validator expects exact headings, so the Explainer Agent instructions had to clearly require all eight sections in the correct order.

Another difficulty was handling configuration and connection errors. The project now checks the topic, Ollama server, and selected model before running the agents.

### Model limitation

I used `qwen2.5-coder:1.5b`, a small local model. It can produce useful explanations, but its output is not always perfectly consistent.

Sometimes it may:

- Omit a required Markdown heading.
- Add extra text before or after the requested sections.
- Produce a less detailed explanation than a larger model.
- Need a prompt to be repeated or simplified.

Because of these limitations, the project validates the required sections before saving the final file.

## Known Limitations

- The project depends on a local Ollama server.
- The selected model must already be installed with `ollama pull`.
- Small local models may not always follow the requested Markdown format.
- The validator checks the presence of headings, not the quality or correctness of the content.
- The project does not automatically correct an invalid study guide.
- The output can vary between runs because LLM generation is not fully deterministic.
- The project is designed for small, beginner-friendly programming topics, not large applications or external services.
