"""
Configuration settings for the Lean AI Assistant.

Created by: Saqeb Newaz
"""

import os
from typing import Dict, List

# Supported frameworks
FRAMEWORKS: Dict[str, str] = {
    '1': 'Toyota Production System (TPS)',
    '2': 'Ford Production System (FPS)',
    '3': 'Stellantis Production Way (SPW)',
    '4': 'Lean Six Sigma (LSS)'
}

# Industry examples for user guidance
INDUSTRY_EXAMPLES: List[str] = [
    "Automotive", "Electronics", "Pharmaceuticals", "Mining & Metals",
    "Aerospace", "Food Processing", "Textile/Apparel", "Medical Devices",
    "Consumer Goods", "Renewable Energy", "Biotech", "Construction Materials",
    "Chemicals", "Plastics & Composites", "Agriculture Equipment",
    "Defense Manufacturing", "Industrial Machinery"
]

# Default AI provider (can be overridden by environment variable)
DEFAULT_AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")

# Application settings
APP_NAME = "Next-Gen Lean AI Assistant"
VERSION = "2.0.0"
AUTHOR = "Saqeb Newaz"