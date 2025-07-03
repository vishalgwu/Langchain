import os
os.environ["OPENAI_API_KEY"]="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"

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchResults
search_tool=DuckDuckGoSearchResults()

@tool
def weather_tool(city:str) -> str:
    """ This will return the weather of the city """
    url = f'https://api.weatherstack.com/current?access_key=8d961077224d99c761cb60aab5ac75c3&query={city}'


    response = requests.get(url)

    return response.json()

llm= ChatOpenAI()
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
prompt= hub.pull("hwchase17/react")

agent1= create_react_agent(
    llm=llm,
    tools=[weather_tool,search_tool],
    prompt=prompt
)

execute_agent=AgentExecutor(
    agent=agent1,
    tools=[search_tool,weather_tool],
    verbose=True
)


response = execute_agent.invoke({"input": "Find the capital of Maharashtra, then find it's current weather condition"})
print(response)

response['output']




