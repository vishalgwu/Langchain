from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# ✅ Step 1: Define schema using Pydantic
class FactSchema(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

parser = PydanticOutputParser(pydantic_object=FactSchema)

# ✅ Step 2: Setup LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# ✅ Step 3: Create prompt with format instructions
template = PromptTemplate(
    template="Give 3 facts about {topic} in structured JSON format.\n\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# ✅ Step 4: Chain everything together
chain = template | model | parser

# ✅ Step 5: Run
result = chain.invoke({"topic": "black hole"})
print(result)
