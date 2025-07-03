import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load Hugging Face token from .env
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  # or use HF_TOKEN if that's your key name

# Initialize Menlo/Jan-nano via Featherless AI provider
client = InferenceClient(
    provider="featherless-ai",
    api_key=hf_token
)

# Streamlit UI
st.title("🧠 Menlo Jan-nano via Hugging Face API")

user_input = st.text_area("💬 Ask anything (e.g., 'Summarize Word2Vec paper'):")

if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            completion = client.chat.completions.create(
                model="Menlo/Jan-nano",
                messages=[{"role": "user", "content": user_input}]
            )
            response = completion.choices[0].message.content
            st.subheader("📌 Result:")
            st.write(response)
    else:
        st.warning("Please enter a valid prompt.")
