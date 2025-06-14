# ai.py
import os
import requests
import certifi
# print("DEBUG: ASI1_MINI_API_KEY =", os.getenv("ASI1_MINI_API_KEY"))

# Grab your key from the environment
API_KEY = os.getenv("ASI1_MINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Please set your ASI1_MINI_API_KEY environment variable")

# Your ASI1 Mini endpoint
API_URL = "https://asi1.ai/dashboard/api-keys"

def call_gpt(prompt: str) -> str:
    """Send prompt to ASI1 Mini and return the assistant’s reply."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "asi1-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    resp = requests.post(API_URL, json=payload, headers=headers)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
