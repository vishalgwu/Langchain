from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

# Setup LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Prompt 1: Detailed report
template_report = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)

# Prompt 2: Summary
template_summary = PromptTemplate(
    template="Write a 5-line summary on the following text:\n{text}",
    input_variables=["text"]
)

# ✅ Chain: report → model → extract content → summary → model
chain = (
    template_report
    | model
    | (lambda x: {"text": x.content})  # Map model output to next prompt input
    | template_summary
    | model
)

result = chain.invoke({"topic": "black hole"})
print(result.content)
