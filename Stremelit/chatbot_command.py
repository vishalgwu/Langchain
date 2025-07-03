import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


load_dotenv()
hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

client = InferenceClient(
    provider="featherless-ai",
    api_key=hf_token,
)


model_id = "mistralai/Magistral-Small-2506"


chat_history = []

print("🤖 Magistral Chatbot (type 'exit' to quit)")
print("----------------------------------------")

while True:
    user_input = input("🧑 You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Exiting chat. Bye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=chat_history,
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"

    chat_history.append({"role": "assistant", "content": bot_reply})
    print(f"🤖 Bot: {bot_reply}\n")

