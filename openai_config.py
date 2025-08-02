import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(description):
    prompt = f"A user submitted a support ticket: \"{description}\". Suggest a helpful support agent reply and classify it."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message.content.strip()

    # Basic rule-based category logic
    if "payment" in description.lower():
        category = "Billing"
    elif "error" in description.lower() or "crash" in description.lower():
        category = "Technical"
    else:
        category = "General"

    return reply, category
