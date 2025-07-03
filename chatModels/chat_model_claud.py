from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

mode= ChatAnthropic(model='claude-3-5-sonnet-20241022', temperature=0, max_tokens_to_sample=10)


result= model.invoke("what is the capital of india ")

print(result)


