from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="""
You are a helpful assistant. Please respond in JSON format like this:
{{
  "joke": "<your generated joke>"
}}

Now, write a joke about {topic}.
""",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {joke}",
    input_variables=["joke"]
)

response_schemas = [
    ResponseSchema(name="joke", description="A funny joke about the topic")
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# correct chaining
chain = prompt1 | model | parser | prompt2 | model

result = chain.invoke({"topic": "AI"})
print(result)
