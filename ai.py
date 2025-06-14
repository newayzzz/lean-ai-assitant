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
## API_URL = "https://asi1.ai/dashboard/api-keys" ##

# Allow override via ASI1_MINI_API_URL environment variable so the client
# can point to the correct API without modifying code.  Fall back to the
# standard chat completion URL.
API_URL = os.getenv(
    "https://asi1.ai/dashboard/api-keys",
    "https://asi1.ai/chat",
)

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

    # resp = requests.post(API_URL, json=payload, headers=headers) ##
    # resp.raise_for_status()                                      ##
    # return resp.json()["choices"][0]["message"]["content"]       ##
    
    try:
        resp = requests.post(API_URL, json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except requests.RequestException as exc:
        return f"Error contacting ASI1 Mini API: {exc}"
    except (KeyError, ValueError) as exc:
        return f"Invalid response from ASI1 Mini API: {exc}"

