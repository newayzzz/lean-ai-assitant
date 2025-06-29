# Next-Gen Lean AI Assistant

A comprehensive command-line tool that provides AI-powered guidance on Lean manufacturing frameworks including Toyota Production System (TPS), Ford Production System (FPS), Stellantis Production Way (SPW), and Lean Six Sigma (LSS).

## 🚀 Features

- **Multi-AI Provider Support**: Choose between OpenAI ChatGPT-4o (default) or ASI1 Mini
- **Industry-Specific Guidance**: Tailored advice for 16+ manufacturing industries
- **Interactive Framework Exploration**: Deep-dive into specific Lean methodologies
- **Implementation Roadmaps**: 6-month phased implementation plans
- **AI Integration Recommendations**: Modern AI tools for Lean manufacturing
- **Canadian Context**: Localized examples and regulatory considerations
- **Crisis Communication Integration**: Emergency protocols for manufacturing environments

## 📋 Requirements

- Python 3.8 or higher
- Internet connection for API calls
- Valid API key for chosen AI provider

## 🛠️ Installation

1. **Clone or download the repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your API keys
   nano .env
   ```

4. **Configure your API keys in `.env`:**
   ```env
   # For OpenAI ChatGPT-4o (recommended)
   OPENAI_API_KEY=your_openai_api_key_here
   
   # For ASI1 Mini (alternative)
   ASI1_MINI_API_KEY=your_asi1_mini_key_here
   ```

## 🎯 Usage

### Basic Usage (OpenAI ChatGPT-4o - Default)
```bash
python main.py
```

### Use ASI1 Mini Provider
```bash
python main.py asi1
```

### Use OpenAI Provider Explicitly
```bash
python main.py openai
```

## 🏭 Supported Industries

- Automotive
- Electronics  
- Pharmaceuticals
- Mining & Metals
- Aerospace
- Food Processing
- Textile/Apparel
- Medical Devices
- Consumer Goods
- Renewable Energy
- Biotech
- Construction Materials
- Chemicals
- Plastics & Composites
- Agriculture Equipment
- Defense Manufacturing
- Industrial Machinery

## 🔧 Supported Frameworks

1. **Toyota Production System (TPS)** - The original Lean methodology
2. **Ford Production System (FPS)** - Ford's adaptation of Lean principles
3. **Stellantis Production Way (SPW)** - Modern automotive Lean approach
4. **Lean Six Sigma (LSS)** - Combined Lean and Six Sigma methodology

## 📊 What You Get

### Framework Guidance
- Core principles explanation
- Industry-specific implementation strategies
- Real-world Canadian case studies
- Interactive learning options

### Implementation Support
- 6-month phased roadmap
- SMART KPIs with AI integration targets
- Change management strategies
- Regulatory compliance checklists

### AI Integration
- Predictive maintenance tools
- Computer vision quality control
- Supply chain optimization platforms
- Real-time analytics solutions
- Crisis communication systems

## 🔧 Architecture

The application is built with a modular architecture:

- `main.py` - Main application and user interface
- `ai_providers.py` - AI service integrations (OpenAI, ASI1 Mini)
- `config.py` - Application configuration and constants
- `prompts.py` - AI prompt templates
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (API keys)

## 🚨 Troubleshooting

### API Key Issues
```bash
# Check if your API key is loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('OpenAI:', bool(os.getenv('OPENAI_API_KEY'))); print('ASI1:', bool(os.getenv('ASI1_MINI_API_KEY')))"
```

### Connection Issues
- Verify internet connectivity
- Check API service status
- Ensure API quotas aren't exceeded

### Provider Fallback
The application automatically falls back to ASI1 Mini if OpenAI fails to initialize.

## 🔒 Security

- API keys are stored in environment variables
- No sensitive data is logged
- HTTPS connections for all API calls
- Request timeouts prevent hanging connections

## 📈 Version History

- **v2.0.0** - Multi-provider support, modular architecture, enhanced prompts
- **v1.0.0** - Initial release with ASI1 Mini integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the GitHub issues
3. Create a new issue with detailed information

---

**Made with ❤️ for the manufacturing community**