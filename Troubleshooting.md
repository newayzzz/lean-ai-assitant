# Troubleshooting Guide

## 🔑 API Key Issues

### 1. API Key Not Found
Check if your environment variables are properly set:

```bash
# Check environment variables
echo $OPENAI_API_KEY
echo $ASI1_MINI_API_KEY
```

If nothing prints, your keys aren't set. Fix by:

```bash
# Option 1: Export in current session
export OPENAI_API_KEY=your_key_here
export ASI1_MINI_API_KEY=your_key_here

# Option 2: Add to shell profile (permanent)
echo 'export OPENAI_API_KEY=your_key_here' >> ~/.bashrc
echo 'export ASI1_MINI_API_KEY=your_key_here' >> ~/.bashrc
source ~/.bashrc
```

### 2. Verify Runtime Loading
Add debug code to check what Python sees:

```python
import os
from dotenv import load_dotenv

load_dotenv()
print("OpenAI Key:", repr(os.getenv("OPENAI_API_KEY")))
print("ASI1 Key:", repr(os.getenv("ASI1_MINI_API_KEY")))
```

### 3. .env File Setup
Ensure your `.env` file is in the project root:

```bash
# Check if .env exists
ls -la .env

# Create from example if missing
cp .env.example .env
nano .env
```

Your `.env` should look like:
```env
OPENAI_API_KEY=sk-your-actual-openai-key-here
ASI1_MINI_API_KEY=your-actual-asi1-key-here
```

## 🌐 Connection Issues

### 1. SSL Certificate Problems
If you encounter SSL errors:

```bash
# Install/update certificates
pip install --upgrade certifi requests

# Or use system certificates
pip install --upgrade requests[security]
```

### 2. Proxy/Firewall Issues
If behind corporate firewall:

```bash
# Set proxy environment variables
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=https://your-proxy:port
```

### 3. Timeout Issues
The application uses 30-second timeouts. If you have slow internet:

Edit `ai_providers.py` and increase timeout:
```python
response = requests.post(self.api_url, json=payload, headers=headers, timeout=60)
```

## 🤖 AI Provider Issues

### 1. OpenAI API Errors

**Rate Limit Exceeded:**
```
Error contacting OpenAI API: 429 Client Error
```
- Wait a few minutes and try again
- Check your OpenAI usage dashboard
- Consider upgrading your OpenAI plan

**Invalid API Key:**
```
Error contacting OpenAI API: 401 Client Error
```
- Verify your API key is correct
- Check if key has expired
- Ensure key has proper permissions

**Model Not Available:**
```
Error contacting OpenAI API: 404 Client Error
```
- Verify GPT-4o access in your OpenAI account
- Try switching to ASI1 provider: `python main.py asi1`

### 2. ASI1 Mini API Errors

**Connection Failed:**
```
Error contacting ASI1 Mini API: Connection error
```
- Check ASI1 service status
- Verify API endpoint URL
- Try again in a few minutes

### 3. Provider Fallback
The app automatically falls back to ASI1 if OpenAI fails. To force a specific provider:

```bash
# Force OpenAI
python main.py openai

# Force ASI1
python main.py asi1
```

## 📦 Dependency Issues

### 1. Missing Dependencies
```bash
# Install all requirements
pip install -r requirements.txt

# Or install individually
pip install requests python-dotenv openai
```

### 2. Version Conflicts
```bash
# Create virtual environment
python -m venv lean_ai_env
source lean_ai_env/bin/activate  # Linux/Mac
# or
lean_ai_env\Scripts\activate     # Windows

# Install dependencies in clean environment
pip install -r requirements.txt
```

### 3. Python Version Issues
Ensure Python 3.8+:
```bash
python --version
# Should show 3.8.0 or higher
```

## 🐛 Runtime Errors

### 1. Import Errors
```python
ModuleNotFoundError: No module named 'dotenv'
```
Solution:
```bash
pip install python-dotenv
```

### 2. JSON Decode Errors
```
Invalid response from API: Expecting value
```
- Usually indicates API returned HTML error page
- Check your API keys and quotas
- Verify internet connection

### 3. Keyboard Interrupt Handling
The app handles Ctrl+C gracefully. If it doesn't exit cleanly:
```bash
# Force kill if needed
pkill -f "python main.py"
```

## 🔧 Configuration Issues

### 1. Wrong Provider Selected
```bash
# Check available providers
python -c "from ai_providers import get_ai_provider; print('Available providers: openai, asi1, chatgpt')"
```

### 2. Environment Variable Override
You can override settings via environment:
```bash
export AI_PROVIDER=asi1
export OPENAI_API_URL=https://custom-endpoint.com/v1/chat/completions
python main.py
```

### 3. Debug Mode
Add debug prints to see what's happening:

```python
# Add to main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🆘 Getting Help

### 1. Check Logs
The application prints detailed error messages. Look for:
- API response codes (401, 429, 500, etc.)
- Connection timeouts
- JSON parsing errors

### 2. Test API Keys Manually
```bash
# Test OpenAI key
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model":"gpt-4o","messages":[{"role":"user","content":"test"}],"max_tokens":5}' \
     https://api.openai.com/v1/chat/completions
```

### 3. Minimal Test Script
Create `test_ai.py`:
```python
from ai_providers import get_ai_provider

try:
    ai = get_ai_provider("openai")
    response = ai.call("Hello, world!")
    print("Success:", response[:100])
except Exception as e:
    print("Error:", e)
```

### 4. Common Solutions Summary

| Problem | Solution |
|---------|----------|
| No API key | Set in `.env` file |
| SSL errors | Update `certifi` package |
| Rate limits | Wait or upgrade plan |
| Import errors | Install missing packages |
| Connection timeout | Check internet/proxy |
| Invalid response | Verify API key/quota |

### 5. Still Need Help?
1. Check the GitHub issues page
2. Create a new issue with:
   - Error message (remove API keys!)
   - Python version
   - Operating system
   - Steps to reproduce

---

**Remember: Never share your actual API keys in issues or support requests!**