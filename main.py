import argparse
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.explainer_agent import explainer_agent
from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections


APP_NAME = "explainer_app"
USER_ID = "student"
SESSION_ID = "explainer-session"
OUTPUT_FILE = "output/explainer_output.md"


async def ask_agent(topic: str) -> str:
    """Send a topic to the Explainer Agent and return its final response."""
    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        agent=explainer_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text=(
                    f"Create a beginner-friendly Markdown study guide "
                    f"for this topic: {topic}"
                )
            )
        ],
    )

    response = "The agent did not return a response."

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response = part.text.strip()
                    break

            if response != "The agent did not return a response.":
                break

    return response


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Create a Markdown study guide for a programming topic."
        )
    )

    parser.add_argument(
        "topic",
        nargs="?",
        default="Python decorators",
        help="Programming topic to explain",
    )

    args = parser.parse_args()

    print(f"Generating study guide for: {args.topic}\n")

    markdown_output = asyncio.run(ask_agent(args.topic))

    print(markdown_output)
    print()

    validation = validate_required_sections(markdown_output)

    if validation["is_valid"]:
        save_result = save_markdown_file(OUTPUT_FILE, markdown_output)
        print(save_result)
    else:
        missing = ", ".join(validation["missing_sections"])
        print(f"The study guide is incomplete. Missing sections: {missing}")


if __name__ == "__main__":
    main()
