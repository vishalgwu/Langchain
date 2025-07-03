from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.runnables import RunnableSequence

load_dotenv()

# LLM setup
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Define output schema
schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic"),
]

# Parser setup
parser = StructuredOutputParser.from_response_schemas(schema)

# Prompt with format injection
template = PromptTemplate(
    template="Give 3 facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# ✅ Chain: template → model → parser
chain = template | model | parser

# Run
result = chain.invoke({"topic": "black hole"})
print(result)
