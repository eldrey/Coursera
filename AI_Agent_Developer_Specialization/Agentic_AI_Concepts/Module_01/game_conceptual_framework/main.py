from GAME import Goal, Action, ActionRegistry, Environment
from GAME import AgentFunctionCallingActionLanguage
from GAME import generate_response
from agent import Agent
import os
from typing import List
import tools
from decorators import PythonActionRegistry
goals = [
    Goal(
        priority=1, 
        name="Explore Files", 
        description="Explore files in the current directory by listing and reading them"
    ),
    Goal(
        priority=2, 
        name="Terminate", 
        description="Terminate the session when tasks are complete with a helpful summary"
    )
]
 # Define tool functions


# # Create action registry and register actions
# action_registry = ActionRegistry()

# action_registry.register(Action(
#     name="list_files",
#     function=list_files,
#     description="Returns a list of files in the directory.",
#     parameters={},
#     terminal=False
# ))

# action_registry.register(Action(
#     name="read_file",
#     function=read_file,
#     description="Reads the content of a specified file in the directory.",
#     parameters={
#         "type": "object",
#         "properties": {
#             "file_name": {"type": "string"}
#         },
#         "required": ["file_name"]
#     },
#     terminal=False
# ))

# action_registry.register(Action(
#     name="write_file",
#     function=write_file,
#     description="Writes content to a specified file in the directory.",
#     parameters={
#         "type": "object",
#         "properties": {
#             "file_name": {"type": "string"},
#             "content": {"type": "string"}
#         },
#         "required": ["file_name", "content"]
#     },
#     terminal=False
# ))

# action_registry.register(Action(
#     name="terminate",
#     function=terminate,
#     description="Terminates the conversation. Prints the provided message for the user.",
#     parameters={
#         "type": "object",
#         "properties": {
#             "message": {"type": "string"},
#         },
#         "required": ["message"]
#     },
#     terminal=True
# ))

# Define the agent language and environment
agent_language = AgentFunctionCallingActionLanguage()
environment = Environment()

# Create the agent
file_explorer_agent = Agent(
    goals=goals,
    agent_language=agent_language,
    action_registry=PythonActionRegistry(tags=["file_management", "file_operations", "system"]),
    generate_response=generate_response,
    environment=environment
)

# Run the agent
user_input = input("What would you like me to do? ")
final_memory = file_explorer_agent.run(user_input, max_iterations=10)

# Print the termination message (if any)
for item in final_memory.get_memories():
    print(f"\nMemory: {item['content']}")