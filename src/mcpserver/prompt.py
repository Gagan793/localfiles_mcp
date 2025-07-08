from mcp.server.fastmcp import FastMCP

mcpserver = FastMCP("FilePrompt")

@mcpserver.prompt()
def prompt_create_file(filename: str, content: str) -> str:
    """
    Generate a prompt to create a new file with the given content.
    
    Args:
        filename: Name of the file to create (e.g., 'todo.txt').
        content: Initial content to write to the file.
    """
    return f"Create a file named '{filename}' with the following content:\n\n{content}"

@mcpserver.prompt()
def prompt_append_to_file(filename: str, new_content: str) -> str:
    """
    Generate a prompt to append content to an existing file.
    
    Args:
        filename: Name of the file to append to.
        new_content: Content to be appended.
    """
    return f"Append the following text to the file '{filename}':\n\n{new_content}"

@mcpserver.prompt()
def prompt_read_file(filename: str) -> str:
    """
    Generate a prompt to read the contents of a file.
    
    Args:
        filename: Name of the file to read.
    """
    return f"Read and display the contents of the file named '{filename}'."

def main():
    mcpserver.run()
