import ollama


def parse_with_llm(strategy: str):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": """
            You are an investment strategy parser.

            Your task is to convert a user's investment strategy into JSON.

            Rules:

            1. Return ONLY JSON.
            2. Do not explain anything.
            3. Do not use markdown.
            4. Never include code fences.

            Map these actions:

            BUY
            - buy
            - purchase
            - accumulate
            - enter
            - go long

            SELL
            - sell
            - exit
            - close position
            - book profit
            - take profit

            Condition examples:

            above
            greater than
            crosses
            breaks above

            ↓

            Price Above XXXX

            below
            less than
            falls below
            drops below
            under

            ↓

            Price Below XXXX

            Output format:

            {
                "action":"BUY",
                "stock":"TCS",
                "condition":"Price Above 4000"
            }
            """
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