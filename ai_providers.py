"""
AI Provider modules for different AI services.
Supports both ASI1 Mini and OpenAI ChatGPT-4o.

Created by: Saqeb Newaz
"""

import os
import requests
from abc import ABC, abstractmethod
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AIProvider(ABC):
    """Abstract base class for AI providers."""
    
    @abstractmethod
    def call(self, prompt: str) -> str:
        """Send prompt to AI service and return response."""
        pass


class ASI1MiniProvider(AIProvider):
    """ASI1 Mini API provider."""
    
    def __init__(self):
        self.api_key = os.getenv("ASI1_MINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("Please set your ASI1_MINI_API_KEY environment variable")
        
        self.api_url = os.getenv(
            "ASI1_MINI_API_URL",
            "https://asi1.ai/chat"
        )
    
    def call(self, prompt: str) -> str:
        """Send prompt to ASI1 Mini and return the assistant's reply."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "asi1-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.RequestException as exc:
            return f"Error contacting ASI1 Mini API: {exc}"
        except (KeyError, ValueError) as exc:
            return f"Invalid response from ASI1 Mini API: {exc}"


class OpenAIProvider(AIProvider):
    """OpenAI ChatGPT-4o API provider."""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("Please set your OPENAI_API_KEY environment variable")
        
        self.api_url = os.getenv(
            "OPENAI_API_URL",
            "https://api.openai.com/v1/chat/completions"
        )
    
    def call(self, prompt: str) -> str:
        """Send prompt to OpenAI ChatGPT-4o and return the assistant's reply."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert Lean manufacturing consultant with deep knowledge of TPS, FPS, SPW, and Lean Six Sigma frameworks. Provide practical, actionable advice for factory floor optimization. Created by Saqeb Newaz."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 2000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.RequestException as exc:
            return f"Error contacting OpenAI API: {exc}"
        except (KeyError, ValueError) as exc:
            return f"Invalid response from OpenAI API: {exc}"


def get_ai_provider(provider_name: str = "openai") -> AIProvider:
    """Factory function to get AI provider instance."""
    providers = {
        "asi1": ASI1MiniProvider,
        "openai": OpenAIProvider,
        "chatgpt": OpenAIProvider,  # Alias for OpenAI
    }
    
    provider_class = providers.get(provider_name.lower())
    if not provider_class:
        available = ", ".join(providers.keys())
        raise ValueError(f"Unknown provider '{provider_name}'. Available: {available}")
    
    return provider_class()