import os
import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def generate_reply(description):
    prompt = f"User: {description}\nSupport Agent:"
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        reply = result[0]['generated_text'].replace(prompt, "").strip()

        # Rule-based categorization
        if "payment" in description.lower():
            category = "Billing"
        elif "error" in description.lower() or "crash" in description.lower():
            category = "Technical"
        else:
            category = "General"

        return reply, category

    except Exception as e:
        return f"⚠️ Error generating reply: {str(e)}", "Error"
