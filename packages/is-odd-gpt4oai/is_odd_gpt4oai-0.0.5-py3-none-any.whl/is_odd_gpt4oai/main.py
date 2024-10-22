from openai import OpenAI
import os

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("API_KEY")
)

def is_odd_gpt4o(number):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": f"Is {number} odd or even? The answer should be true or false only. No additional characters.",
            }
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=4096,
        top_p=1
    )
    return response.choices[0].message.content