from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loader= DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

result = list(loader.lazy_load())

print(result[0].metadata)
print(len(result))

for docs in result:
    print(docs.metadata)



