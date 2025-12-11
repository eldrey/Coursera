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


messages = [
    {"role": "system", "content": "You are an expert software engineer."},
]

def extract_code_block(response: str) -> str:
    """Extract code block from response"""
    if not '```' in response:
        return response

    code_block = response.split('```')[1].strip()
    if code_block.startswith("python"):
        code_block = code_block[6:]

    return code_block

def extract_documentation_block(response: str) -> str:
    """Extract documentation block from response"""
    docstring_match = re.search(r'"""(.*?)"""', response, re.DOTALL)
    if docstring_match:
        return docstring_match.group(0)
    return ""

if __name__ == "__main__":
    function = "A function that takes a word and returns all possible palindromes within that word In Python" #input("What function do you want to create? ")
    messages.append({"role":"user", "content": f"Write only a basic Python function, without comments, examples, or descriptions, based on this description: {json.dumps(function)}"})

    response = generate_response(messages)
    print("================ First response =================")
    print(response)
    messages.append({"role": "assistant", "content": extract_code_block(response)})
    messages.append({"role": "user", "content": "Update the function to include documentation."})
    print("================ Second response =================")
    response = generate_response(messages)
    print(response)
    print("================ Third response =================")
    messages.append({"role": "assistant", "content": extract_documentation_block(response)})
    messages.append({"role": "user", "content": "Using Python's unittest framework, write unit tests for the function."})
    response = generate_response(messages)
    print(response)




