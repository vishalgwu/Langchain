from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
load_dotenv()

# LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Prompts
prompt1 = PromptTemplate(
    template="Generate a tweet about topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about topic {topic}",
    input_variables=["topic"]
)

# Parallel chain with passthrough
parallel_chain = RunnableParallel({
    "original": RunnablePassthrough(),
    "tweet": prompt1 | model,
    "linkedin": prompt2 | model
})

result = parallel_chain.invoke({"topic": "AI"})
print(result)
