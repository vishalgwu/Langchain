import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load Hugging Face token
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Set up MiniMax LLM via Novita provider
client = InferenceClient(
    provider="novita",
    api_key=hf_token
)

st.title("🧠 Research Paper Summarizer (MiniMax LLM)")

# User manually types paper name
paper_input = st.text_input(
    "📄 Enter Research Paper Name",
    placeholder="e.g., Word2Vec: Efficient Estimation of Word Representations"
)

# Explanation style
style_input = st.selectbox(
    "📝 Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Summary length
length_input = st.selectbox(
    "📏 Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Generate summary
if st.button("Summarize"):
    if paper_input.strip():
        prompt = (
            f"Please summarize the research paper titled '{paper_input}' "
            f"in a {style_input.lower()} style. "
            f"Keep the explanation {length_input.lower()}."
        )

        with st.spinner("Generating summary..."):
            response = client.chat.completions.create(
                model="MiniMaxAI/MiniMax-M1-80k",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.subheader("📌 Summary:")
            st.write(result)
    else:
        st.warning("Please enter a research paper title.")
