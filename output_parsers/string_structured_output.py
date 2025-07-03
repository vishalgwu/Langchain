from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# LLM setup
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Output schema
schema = [
    ResponseSchema(name="fact_1", description='Fact 1 about the topic'),
    ResponseSchema(name="fact_2", description='Fact 2 about the topic'),
    ResponseSchema(name="fact_3", description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

# Prompt Template with format instructions
template = PromptTemplate(
    template="Give 3 facts about {topic}.\n\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Build the chain
chain = template | model | parser

# Invoke
result = chain.invoke({"topic": "black hole"})
print(result)
