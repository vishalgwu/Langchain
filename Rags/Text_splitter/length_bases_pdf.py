from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader("MultilayerNetworkChapter.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_documents(docs)
print(f"Total chunks: {len(result)}")
print(result[0].page_content)
print(result[0])