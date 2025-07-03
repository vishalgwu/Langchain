from typing import TypedDict


class person(TypedDict):
    name:str
    age:int

new_person: person={"name":'vishal', "age":20}

print(new_person)