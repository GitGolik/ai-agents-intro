REQUIRED_SECTIONS = [
    "Topic",
    "Simple Explanation",
    "Key Concepts",
    "Example",
    "Practice Exercise",
    "Common Mistakes",
    "Review Comments",
    "Final Summary",
]


def validate_required_sections(markdown: str) -> dict:
    """Check that a Markdown study guide contains all required sections.

    Args:
        markdown: The Markdown content to validate.

    Returns:
        A dictionary with:
        - is_valid: True if every required section is present.
        - missing_sections: A list of missing section names.
    """
    missing_sections = []

    for section in REQUIRED_SECTIONS:
        heading = f"## {section}"

        if heading not in markdown:
            missing_sections.append(section)

    return {
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }
