## Configuration de l’environnement

### Environnement Python

Le venv contient uniquement les dépendances Python du projet.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install google-adk litellm python-dotenv
```

Dépendances installées dans le venv :

- `google-adk`
- `litellm`
- `python-dotenv`

### Ollama

Ollama est installé **en dehors du venv**, au niveau du système.

```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
ollama -v
ollama serve
```

### Modèle local

Modèle utilisé : `qwen2.5-coder:1.5b`

```bash
ollama pull qwen2.5-coder:1.5b
ollama list
ollama run qwen2.5-coder:1.5b
```

Le modèle est téléchargé et géré par Ollama. Il n’est pas installé avec `pip`.

### Test du modèle

```bash
ollama run qwen2.5-coder:1.5b
```

Prompt :

```text
Explique les décorateurs Python en trois phrases.
```

### Variables d’environnement

```bash
cp .env.example .env
```

```text
OLLAMA_API_BASE=http://localhost:11434
MODEL_NAME=ollama_chat/qwen2.5-coder:1.5b
```

### Sécurité

- `.env` n’est jamais commité.
- `.venv/` n’est jamais commité.
- Aucune clé API n’est présente dans le dépôt.


## Explainer Agent example

Command:

```bash
python main.py "Python decorators"
```

Example output:

## Explanation
A decorator is a function that modifies another function without changing its code. It is placed above a function using the `@` symbol.

## Key concepts
- Function
- Wrapper function
- `@decorator` syntax
- Reusable behavior

## Example
```python
def say_hello():
    print("Hello!")

say_hello()
```

This example defines and calls a simple function.
