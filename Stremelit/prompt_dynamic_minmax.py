import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load HF token from .env
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Init MiniMax LLM via Novita provider
client = InferenceClient(
    provider="novita",
    api_key=hf_token
)

st.title("🧠 Research Paper Summarizer (MiniMax)")

# Dropdown 1: Paper topic
paper_input = st.selectbox(
    "📄 Select Research Paper",
    ["Attention Is All You Need",
     "GPT-3: Language Models are Few-Shot Learners",
     "BERT: Pre-training of Deep Bidirectional Transformers",
     "Diffusion Models Beat GANs on Image Synthesis"]
)

# Dropdown 2: Explanation Style
style_input = st.selectbox(
    "📝 Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Dropdown 3: Summary Length
length_input = st.selectbox(
    "📏 Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Generate when button is clicked
if st.button("Summarize"):
    # Create prompt dynamically
    prompt = f"Please summarize the research paper titled '{paper_input}' in a {style_input.lower()} style. Keep the explanation {length_input.lower()}."

    with st.spinner("Summarizing with MiniMax..."):
        response = client.chat.completions.create(
            model="MiniMaxAI/MiniMax-M1-80k",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        st.subheader("📌 Summary:")
        st.write(result)
