import argparse
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.explainer_agent import explainer_agent


APP_NAME = "explainer_app"
USER_ID = "student"
SESSION_ID = "explainer-session"


async def ask_agent(topic: str) -> str:
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
        parts=[types.Part(text=f"Explain this topic: {topic}")],
    )

    final_response = "The agent did not return a response."

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text.strip()
            break

    return final_response


def main():
    parser = argparse.ArgumentParser(
        description="Explain a programming topic with the Explainer Agent."
    )
    parser.add_argument(
        "topic",
        nargs="?",
        default="Python decorators",
        help="Topic to explain",
    )
    args = parser.parse_args()

    response = asyncio.run(ask_agent(args.topic))
    print(response)


if __name__ == "__main__":
    main()
