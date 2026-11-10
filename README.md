## Troubleshooting

### Missing environment variables

If you see:

```text
Missing required environment variable: OLLAMA_API_BASE
```

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Then set:

```env
OLLAMA_API_BASE=http://localhost:11434
OLLAMA_MODEL=qwen2.5-coder:1.5b
```

### Ollama is not running

If you see:

```text
Cannot connect to Ollama at http://localhost:11434
```

Start Ollama:

```bash
ollama serve
```

Then verify:

```bash
ollama list
```

### Model is not available

If you see:

```text
Ollama model 'qwen2.5-coder:1.5b' is not available
```

Install the model:

```bash
ollama pull qwen2.5-coder:1.5b
```

You can also use another installed model by changing `OLLAMA_MODEL` in `.env`.

### Empty topic

Run the program with a topic:

```bash
python main.py "Python decorators"
```

### Validation failure

If you see:

```text
The study guide is incomplete. Missing sections: ...
```

Run the command again. Local models can sometimes omit a required Markdown heading.

### File-writing error

If you see a file-writing error, check that the `output/` directory is writable and that you have enough disk space.
