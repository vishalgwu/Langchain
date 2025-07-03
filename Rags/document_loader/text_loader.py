from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loader=TextLoader('business.txt',encoding='utf-8')

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0])
print(type(docs[0]))

prompt=PromptTemplate(
    template=" write a summary for the following poem- \\n {poem}",
    input_variables=['poem']
    
)

parser= StrOutputParser()

chain =prompt| model | parser

result= chain.invoke({'poem': docs[0].page_content})

print(result)