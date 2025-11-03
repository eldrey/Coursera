from litellm import completion
from typing import List, Dict
import json
import re
def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="gemini/gemini-2.5-flash",
        messages=messages
    )
    return response.choices[0].message.content

def parser_code(response:str):
    code_pattern = r"```(?:\w+\n)?(.*?)```"
    response = re.findall(code_pattern, response, re.DOTALL)
    response = "\n\n".join([c.strip() for c in response])
    # response = response.split("```")[1]
    response = re.sub(r"(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\')", "", response)
    
    return response

messages = [
    {"role": "system", "content": "You are an expert software engineer."},
]


if __name__ == "__main__":
    function = "A function that takes a word and returns all possible palindromes within that word python" #input("What function do you want to create? ")
    messages.append({"role":"user", "content": f"Write a basic python function based on this description: {json.dumps(function)}"})

    response = generate_response(messages)
    print(parser_code(response))



