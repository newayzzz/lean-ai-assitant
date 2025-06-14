Troubleshooting

1. **API-Key Not Found**

```bash
echo $ASI1_MINI_API_KEY
```

If that prints nothing, re-export in your shell or add it to `~/.zshrc` / `.bash_profile`, then `source` that file.

2. **Verify at Runtime**
Add at the top of `ai.py` to see exactly what Python sees:

```python
import os
print("DEBUG: ASI1_MINI_API_KEY =", repr(os.getenv("ASI1_MINI_API_KEY")))
```

3. **.env Support**

```bash
pip install python-dotenv
```

Create a `.env` file:

```env
ASI1_MINI_API_KEY=your_real_key_here
```

And add to `ai.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

4. **SSL Certificate Issues**
If you hit SSL errors, install certifi and force its bundle:

```bash
pip install certifi
```

```python
import certifi
resp = requests.post(API_URL, json=payload, headers=headers, verify=certifi.where())
```

5. **Quick Bypass** (not for production)

```python
resp = requests.post(API_URL, json=payload, headers=headers, verify=False)
```
