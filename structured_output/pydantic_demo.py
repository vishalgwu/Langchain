from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr, Field



class student(BaseModel):
    name:str
    age: Optional[int] = None
    email: EmailStr     
    cgpa : float = Field(gt=0 , lt= 10 , default=5)
    
new_student = { "name": "Vishal", "age": 36, 'email': 'xyz@gmail.com', 'cgpa': 8}

student= student(**new_student)
student_dict=dict(student)
print(student)

print(student_dict['age'])