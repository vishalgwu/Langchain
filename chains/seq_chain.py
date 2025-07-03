from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser  # ✅ Fixed import
from pydantic import BaseModel, Field

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5-point summary for the following text:\n\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()


chain = prompt1 | model | parser | (lambda x: {"text": x}) | prompt2 | model | parser


result = chain.invoke({"topic": "history of Sri Lanka"})

print(result)


chain.get_graph().print_ascii()
