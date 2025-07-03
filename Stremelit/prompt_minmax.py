import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load Hugging Face token
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Create a client for MiniMax via novita provider
client = InferenceClient(
    provider="novita",
    api_key=hf_token  # MiniMax hosted by Novita
)

# Streamlit UI
st.title("🤖 MiniMax Chat LLM via Hugging Face API")

user_input = st.text_area("💬 Enter your prompt (e.g., 'Summarize Word2Vec paper'):")

if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            completion = client.chat.completions.create(
                model="MiniMaxAI/MiniMax-M1-80k",
                messages=[{"role": "user", "content": user_input}]
            )
            response = completion.choices[0].message.content
            st.subheader("📌 Result:")
            st.write(response)
    else:
        st.warning("Please enter a valid prompt.")
