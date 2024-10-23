import argparse
import asyncio
import sys

from llm_taxi.conversation import Message, Role
from llm_taxi.factory import llm


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--model", type=str, default="openai:gpt-3.5-turbo")

    return parser.parse_args()


async def async_main():
    args = parse_args()

    call_options = {
        "max_tokens": args.max_tokens,
    }
    try:
        model = llm(model=args.model, call_options=call_options)
    except KeyError as e:
        print(f"Error: {e}")
        sys.exit(1)

    while True:
        try:
            user_input = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)

        if not user_input:
            continue

        messages = [
            Message(
                role=Role.User,
                content=user_input,
            ),
        ]
        response = await model.streaming_response(messages=messages)

        async for chunk in response:
            print(chunk, end="", flush=True)
        print("\n")


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
