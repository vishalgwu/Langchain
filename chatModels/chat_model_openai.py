from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key="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"
)

result = model.invoke("What is the capital of India?")
print(result)
print(result.content)
