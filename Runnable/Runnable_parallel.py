from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a tweet about topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about topic {topic}",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel({
    'tweet': prompt1 | model,
    'linkedin': prompt2 | model
})

result = parallel_chain.invoke({"topic": "AI"})
print(result)
