from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from huggingface_hub import login
from dotenv import load_dotenv
import os

# Load .env and login to Hugging Face
load_dotenv()
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# Use Hugging Face Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Sample docs
documents = [
    Document(page_content="The capital of India is Delhi."),
    Document(page_content="The capital of France is Paris."),
    Document(page_content="The capital of Germany is Berlin.")
]

# Vector DB
db = FAISS.from_documents(documents, embedding_model)

# Query
query = "What is the capital of India?"
results = db.similarity_search(query, k=1)

# Output
print("✅ Top Match:", results[0].page_content)
