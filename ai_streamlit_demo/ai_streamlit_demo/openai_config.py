import openai

# ⚠️ Replace with your actual OpenAI key here
openai.api_key = "sk-..."

def generate_reply(description):
    prompt = f"A user submitted a support ticket: \"{description}\". Suggest a helpful support agent reply and classify it."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content.strip()

    # Simple keyword-based category guess
    if "payment" in description.lower():
        category = "Billing"
    elif "error" in description.lower() or "crash" in description.lower():
        category = "Technical"
    else:
        category = "General"

    return reply, category
