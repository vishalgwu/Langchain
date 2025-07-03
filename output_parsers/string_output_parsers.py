from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template_report = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=['topic']
)

template_summary = PromptTemplate(
    template="Write a 5-line summary on the following text:\n{text}",
    input_variables=['text']
)

prompt1 = template_report.invoke({'topic': 'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template_summary.invoke({'text': result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
