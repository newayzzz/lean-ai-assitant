"""
Streamlit Web App for Next-Gen Lean AI Assistant
A comprehensive web interface for AI-powered Lean manufacturing guidance.

Created by: Saqeb Newaz
"""

import streamlit as st
import os
from dotenv import load_dotenv
from main import run_assistant
from config import FRAMEWORKS, INDUSTRY_EXAMPLES, APP_NAME, VERSION, AUTHOR

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Lean AI Assistant",
    page_icon="🏭",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .response-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown(f"""
<div class="main-header">
    <h1>🏭 {APP_NAME}</h1>
    <p>Version {VERSION} | Created by {AUTHOR}</p>
    <p>AI-powered guidance for Lean manufacturing optimization</p>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("## 🔧 Configuration")
    
    # API Provider selection
    provider_options = {
        "OpenAI": "openai",
        "ASI1 Mini": "asi1"
    }
    selected_provider = st.selectbox(
        "🤖 Choose AI Provider",
        options=list(provider_options.keys())
    )
    provider = provider_options[selected_provider]
    
    # API Key status
    st.markdown("## 🔑 API Key Status")
    openai_key = os.getenv("OPENAI_API_KEY")
    asi1_key = os.getenv("ASI1_MINI_API_KEY")
    
    if openai_key:
        st.success("✅ OpenAI API Key loaded")
    else:
        st.error("❌ OpenAI API Key missing")
    
    if asi1_key:
        st.success("✅ ASI1 Mini API Key loaded")
    else:
        st.error("❌ ASI1 Mini API Key missing")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 🔧 Select Lean Framework")
    
    framework_options = [
        "Toyota Production System (TPS)",
        "Ford Production System (FPS)",
        "Stellantis Production Way (SPW)",
        "Lean Six Sigma (LSS)"
    ]
    
    framework = st.selectbox(
        "Select Lean Framework",
        options=framework_options
    )
    
    st.markdown("## 🏭 Select Industry")
    
    industry = st.selectbox(
        "Select Industry",
        options=INDUSTRY_EXAMPLES
    )
    
    st.markdown("## 💬 Ask Your Question")
    
    user_input = st.text_area(
        "Ask a Lean-related question:",
        height=150,
        placeholder="Example: How can I reduce waste in my automotive assembly line using TPS principles?"
    )

with col2:
    st.markdown("## 📊 Current Selection")
    st.info(f"""
    **🤖 AI Provider:** {selected_provider}
    
    **📋 Framework:** {framework}
    
    **🏭 Industry:** {industry}
    """)

# Main action button
if st.button("🚀 Run Assistant", type="primary", use_container_width=True):
    if user_input.strip():
        # Check API keys
        if provider == "openai" and not openai_key:
            st.error("❌ OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
        elif provider == "asi1" and not asi1_key:
            st.error("❌ ASI1 Mini API key not found. Please set ASI1_MINI_API_KEY in your .env file.")
        else:
            with st.spinner("🤖 Thinking..."):
                try:
                    output = run_assistant(framework, industry, provider.lower(), user_input)
                    
                    st.markdown("""
                    <div class="response-container">
                        <h3>💡 AI Response</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("Response:")
                    st.write(output)
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question.")

# Footer
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #666;'>Made with ❤️ by {AUTHOR} for the manufacturing community</div>", unsafe_allow_html=True)