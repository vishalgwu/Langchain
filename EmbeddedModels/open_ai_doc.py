from langchain_openai import OpenAIEmbeddings
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
import os
print("✅ Loaded Key:", os.getenv("OPENAI_API_KEY"))

from dotenv import load_dotenv
load_dotenv()

embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


result= embedding.embed_query('dheli is capital of india')
print(str(result))