from pathlib import Path


def save_markdown_file(file_path: str, content: str) -> str:
    """Save Markdown content to a file and return a confirmation message.

    Args:
        file_path: Path where the Markdown file will be saved.
        content: Markdown text to write to the file.

    Returns:
        A success message containing the saved file path.
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(content, encoding="utf-8")

        return f"Markdown file saved successfully at: {path}"
    except OSError as error:
        return f"Error saving Markdown file '{file_path}': {error}"
