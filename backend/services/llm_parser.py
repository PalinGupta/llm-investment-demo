import ollama


def parse_with_llm(strategy: str):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract investment strategy information. "
                    "Return only the requested fields."
                ),
            },
            {
                "role": "user",
                "content": strategy,
            },
        ],
        format={
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "stock": {"type": "string"},
                "condition": {"type": "string"},
            },
            "required": [
                "action",
                "stock",
                "condition",
            ],
        },
    )

    return response.message.content