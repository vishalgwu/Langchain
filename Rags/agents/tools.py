from langchain_community.tools import DuckDuckGoSearchRun

search=DuckDuckGoSearchRun()

result=search.invoke(" what are top news in US")
print(result)

print(search.name)
print(search.description)
print(search.args)


from langchain_core.tools import tool

def devide(a,b):
    """ Devide two numbers"""
    return a/b

def Devide(a: int,b:int)-> int:
    """ devide two numbers"""
    return a/b

@tool
def Devide(a:int,b:int) -> int:
    """Devide two numbers"""
    return a/b

reult=Devide.invoke({"a":9,"b":10})

print(reult)

from langchain.tools import StructuredTool
from pydantic import BaseModel
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")
    
    
def multiply(a: int,b:int) -> int:
    """multiply two numbers"""
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

mul=multiply_tool.invoke({'a': 10,'b':20})

print(mul
      )
print(multiply_tool.name)
print(multiply_tool.description)


#tool kit 
from langchain_core.tools import tool

@tool
def add(a:int,b:int) -> int:
    """ additon of two number s"""
    return a+b

@tool
def multiply(a:int,b:int)-> int:
    """ Multiplication of two numbers"""
    return a*b


class mathtoolkit:
    def tools(self):
        return[add, multiply]


toolkit = mathtoolkit()
tools = toolkit.tools()

for tool in tools:
    print(tool.name, "=>", tool.description)
