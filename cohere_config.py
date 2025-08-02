import os
import cohere

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_reply(description):
    prompt = f"A customer submitted a support ticket: '{description}'. Suggest a polite and helpful response."

    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=100
        )

        reply = response.generations[0].text.strip()

        if "payment" in description.lower():
            category = "Billing"
        elif "error" in description.lower() or "crash" in description.lower():
            category = "Technical"
        else:
            category = "General"

        return reply, category

    except Exception as e:
        return f"⚠️ Error generating reply: {str(e)}", "Error"
