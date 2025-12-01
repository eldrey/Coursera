import os
from typing import List
from decorators import register_tool


@register_tool(tags=["file_management", "list"])
def list_files() -> List[str]:
    """List files in the current directory."""
    return os.listdir(".")

@register_tool(tags=["file_operations", "read"])
def read_file(file_name: str) -> str:
    """Read a file's contents."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."
    except Exception as e:
        return f"Error: {str(e)}"

@register_tool(tags=["file_operations", "write"])
def write_file(file_name: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(file_name, "w") as file:
            file.write(content)
        return f"Successfully wrote to {file_name}."
    except Exception as e:
        return f"Error: {str(e)}"
    
@register_tool(tags=["system"], terminal=True)
def terminate(message: str) -> str:
    """Terminate the agent loop and provide a summary message."""
    return message