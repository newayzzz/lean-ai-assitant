This repository contains a small command line tool for interacting with an API-based chatbot that provides guidance on Lean manufacturing frameworks.

## Features
- Prompts the user for their industry and preferred Lean framework
- Sends the conversation to the ASI1 Mini model via HTTP
- Returns responses with implementation advice, AI tools, and more

## Requirements
- Python 3.8 or higher
- `requests` package
- Environment variable `ASI1_MINI_API_KEY` set to a valid API key

## Usage
Install the required dependency and run the assistant:

```bash
pip install requests
export ASI1_MINI_API_KEY=<your key>
python main.py
```

Follow the prompts to receive Lean framework guidance and additional resources.

