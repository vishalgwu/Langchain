from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser  

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template_report = PromptTemplate(
    template="Give me the name, age, and city of a fictional character.\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template_report.format()
result = model.invoke(prompt)

parsed = parser.invoke(result.content)
print(parsed)
print(type(parsed))
