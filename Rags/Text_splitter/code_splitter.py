from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


text= """from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# load your code file (example: myscript.py)
loader = TextLoader("myscript.py")   # works on .py, .js, .java, etc.
docs = loader.load()

# create a text splitter tuned for code
splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",  # supports "python", "java", "cpp", etc.
    chunk_size=200,     # adjust chunk size to your needs
    chunk_overlap=20
)

# actually split the code
chunks = splitter.split_documents(docs)

print(f"Total code chunks: {len(chunks)}")
print("--- first chunk preview ---")
print(chunks[0].page_content)
"""



spliter= RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)


chunk=spliter.split_text(text)

print(len(chunk))
print(chunk)