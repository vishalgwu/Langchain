import os
import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load token
load_dotenv()
hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize client
client = InferenceClient(
    provider="featherless-ai",
    api_key=hf_token
)

# Title
st.title("🧠 Magistral‑Small Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show conversation
for msg in st.session_state.chat_history:
    prefix = "🧑‍💬 You:" if msg["role"] == "user" else "🤖 Bot:"
    st.markdown(f"**{prefix}** {msg['content']}")

# Chat input at the bottom
with st.form("chat_input_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Ask anything...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# Handle user message
if submitted and user_input.strip():
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Send message to LLM
    try:
        response = client.chat.completions.create(
            model="mistralai/Magistral-Small-2506",
            messages=st.session_state.chat_history
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"

    # Add bot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

    # Rerun to update display
    st.rerun()
