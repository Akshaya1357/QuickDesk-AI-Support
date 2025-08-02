import os
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def generate_reply(description):
    prompt = f"Suggest a helpful customer support reply to: {description}"

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        result = response.json()

        reply = result[0]["generated_text"].strip()

        if "payment" in description.lower():
            category = "Billing"
        elif "error" in description.lower() or "crash" in description.lower():
            category = "Technical"
        else:
            category = "General"

        return reply, category

    except Exception as e:
        return f"⚠️ Error generating reply: {str(e)}", "Error"
