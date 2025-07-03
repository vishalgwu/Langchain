import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct', openai_api_key=os.getenv("OPENAI_API_KEY"))

result = llm.invoke(input="What is the capital of India?")
print(result)


