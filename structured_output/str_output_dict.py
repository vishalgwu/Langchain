
# not working , use open ai api llm. 


from langchain_huggingface.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Define your structured schema
class Review(BaseModel):
    summary: str = Field(description="Summary of the review")
    sentiment: str = Field(description="Sentiment: positive, negative, or neutral")

parser = PydanticOutputParser(pydantic_object=Review)

template = """
Analyze the following movie review and respond in the following JSON format:

Review: "{review}"

Format:
{{
     "summary": "...",
    "sentiment": "positive | neutral | negative"
}}
"""


prompt = PromptTemplate(
    template=template,
    input_variables=["review"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# ✅ Switch to HuggingFaceEndpoint
llm = HuggingFaceEndpoint(
    task="text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    max_new_tokens=300,
    temperature=0.5,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

review_text = "This movie was exciting and beautifully directed. However, the ending felt a bit rushed."
formatted_prompt = prompt.format(review=review_text)
output = llm.invoke(formatted_prompt)
print("Raw output from model:\n", output)

try:
    result = parser.parse(output)
    print(result)
except Exception as e:
    print("Parsing failed:", e)

print("Final Prompt:\n", formatted_prompt)

