from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


documents = [
    Document(page_content="The capital of India is Delhi."),
    Document(page_content="The capital of France is Paris."),git 
    Document(page_content="The capital of Germany is Berlin.")
]


db = FAISS.from_documents(documents, embedding_model)



query = "What is the capital of paris?"
results = db.similarity_search(query, k=1)


print("✅ Top Match:", results[0].page_content)
