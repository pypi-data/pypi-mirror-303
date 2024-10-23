import asyncio

from llm_taxi.conversation import Message, Role
from llm_taxi.factory import embedding, llm


async def main():
    clients = [
        # llm(model="groq:llama3-70b-8192"),
        # llm(model="openai:gpt-3.5-turbo"),
        # llm(model="google:gemini-pro"),
        # llm(model="together:meta-llama/Llama-3-70b-chat-hf"),
        # llm(model="anthropic:claude-2.1"),
        llm(model="mistral:mistral-small"),
        # llm(model="perplexity:llama-3.1-8b-instruct"),
        # llm(model="deepinfra:meta-llama/Meta-Llama-3-8B-Instruct"),
        # llm(model="deepseek:deepseek-chat"),
        # llm(model="openrouter:rwkv/rwkv-5-world-3b"),
        # llm(model="dashscope:qwen-turbo"),
        # llm(model="bigmodel:glm-4-air"),
    ]

    for client in clients:
        print("========================================")
        print(client.model)
        messages = [
            Message(role=Role.User, content="What is the capital of France?"),
        ]

        kwargs = {
            "temperature": 0.1,
            "max_tokens": 100,
            # "top_k": 10,
            "top_p": 0.9,
            "stop": ["."],
            "seed": 0,
        }

        response = await client.response(messages, llm_options=kwargs)
        print(response)

        # client = llm(model="mistral:mistral-small")
        messages = [
            Message(role=Role.User, content="Tell me a joke."),
        ]
        response = await client.streaming_response(messages, llm_options=kwargs)
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

    return

    embedders = [
        embedding(model="openai:text-embedding-ada-002"),
        embedding(model="mistral:mistral-embed"),
        embedding(model="google:models/embedding-001"),
    ]

    for embedder in embedders:
        print("========================================")
        print(embedder.model)
        embeddings = await embedder.embed_text("Hello, world!")
        print(embeddings[:10])
        embeddings = await embedder.embed_texts(["Hello, world!"])
        print(embeddings[0][:10])


if __name__ == "__main__":
    asyncio.run(main())


# import asyncio

# from llm_taxi.conversation import Message, Role
# from llm_taxi.factory import llm


# async def main():
#     clients = [
#         llm(model="openai:gpt-3.5-turbo"),
#         llm(model="google:gemini-pro"),
#         llm(model="together:meta-llama/Llama-3-70b-chat-hf"),
#         llm(model="groq:llama3-70b-8192"),
#         llm(model="anthropic:claude-2.1"),
#         llm(model="mistral:mistral-small"),
#         llm(model="perplexity:llama-3-8b-instruct"),
#         llm(model="deepinfra:meta-llama/Meta-Llama-3-8B-Instruct"),
#         llm(model="deepseek:deepseek-chat"),
#         llm(model="openrouter:rwkv/rwkv-5-world-3b"),
#         llm(model="dashscope:qwen-turbo"),
#     ]

#     for client in clients:
#         messages = [
#             Message(role=Role.User, content="What is the capital of France?"),
#         ]
#         response = await client.response(messages)
#         print(response)

#         response = await client.streaming_response(messages)
#         async for chunk in response:
#             print(chunk, end="", flush=True)


# if __name__ == "__main__":
#     asyncio.run(main())
