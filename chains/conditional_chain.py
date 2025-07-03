from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# LLM setup
llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-3-27b-it",
    task="text-generation"
)
model1 = ChatHuggingFace(llm=llm1)

# Pydantic schema
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)
parser = StrOutputParser()

# Sentiment classification prompt
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback into positive or negative:\n\n{feedback}\n\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

# Prompt for positive feedback
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n\n{feedback}",
    input_variables=["feedback"]
)

# Prompt for negative feedback
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n\n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model1 | parser),
    RunnableLambda(lambda _: "Could not find any sentiment.")
)


# Complete chain
chain = classifier_chain | branch_chain

# Run
result = chain.invoke({'feedback': 'this is a terrible phone'})
print(result)
chain.get_graph().print_ascii()