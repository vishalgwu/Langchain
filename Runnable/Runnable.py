import random

class NakaliLLM:
    def __init__(self):
        print("LLM created")
        
    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "AI stands for Artificial Intelligence",
            "IPL is a cricket league"
        ]
        return {'response': random.choice(response_list)}

llm = NakaliLLM()
print(llm.predict('What is the capital of India?'))


class NakaliPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
        
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
# Create the template
template = NakaliPromptTemplate(
    template="Write a poem about {topic}.",
    input_variables=['topic']
)

# Format the prompt
formatted_prompt = template.format({'topic': 'India'})
print(formatted_prompt)
