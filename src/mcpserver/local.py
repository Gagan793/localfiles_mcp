import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")

# Define a default base directory if no specific directory is provided by the user.
# This path is relative to your home directory (~).
DEFAULT_STORAGE_BASE = "~/Desktop/LOCAL_MCP/claude_local_notes"

# Helper function to resolve the user-provided directory path
def _resolve_directory_path(user_provided_directory: str | None) -> str:
    """
    Resolves a user-provided directory string into a safe, absolute path,
    relative to the user's home directory.
    If no directory is provided, it uses the DEFAULT_STORAGE_BASE.
    Ensures the path is within the user's home directory for security.
    """
    home_dir = os.path.expanduser("~") # Get the absolute path to your home directory

    if user_provided_directory:
        # Expand user (~) if present in the user-provided path
        expanded_path = os.path.expanduser(user_provided_directory)

        # If the path is not absolute (doesn't start with /), assume it's relative to home
        if not os.path.isabs(expanded_path):
            resolved_path = os.path.join(home_dir, expanded_path)
        else:
            resolved_path = expanded_path # Use the absolute path as is

        # --- IMPORTANT SECURITY CHECK ---
        # This prevents the tool from writing to arbitrary system locations
        # outside your home directory (e.g., /etc, /usr) which could be risky.
        if not resolved_path.startswith(home_dir):
            raise ValueError(f"Invalid directory path: '{user_provided_directory}'. For security, target directory must be within your home directory.")
        # --- END SECURITY CHECK ---

        abs_path = resolved_path
    else:
        # If no directory is provided, use the default storage base
        abs_path = os.path.expanduser(DEFAULT_STORAGE_BASE)

    # Create the directory if it doesn't exist
    os.makedirs(abs_path, exist_ok=True)
    return abs_path

# --- Tool Functions Updated ---

@mcp.tool()
def create_new_file(filename: str, content: str, directory: str = None) -> str: # type: ignore
    """
    Creates a new file with the given name and content in the specified directory.
    If the file already exists, it will be overwritten.
    If no directory is specified, it defaults to a predefined storage location.

    Args:
        filename: Name of the file to create (e.g., 'todo.txt').
        content: Initial content to write to the file.
        directory: Optional. The path to the directory (e.g., 'Desktop', 'Documents/MyFiles', '~/my_folder').
                   Paths are resolved relative to your home directory (~).
                   For security, paths must be within your home directory.
    """
    try:
        target_dir = _resolve_directory_path(directory)
        full_path = os.path.join(target_dir, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"File '{filename}' created successfully in '{target_dir}'."

    except ValueError as ve: # Catch validation errors from _resolve_directory_path
        return f"Error creating file: {ve}"
    except Exception as e:
        # Provide the full_path in the error message for better debugging if something goes wrong
        return f"Error creating file '{filename}' in '{target_dir}': {e}" # type: ignore

@mcp.tool()
def add_note_to_file(content: str, filename: str = "notes.txt", directory: str = None) -> str: # type: ignore
    """
    Appends the given content to the specified file in the specified directory.
    If no directory is specified, it defaults to a predefined storage location.

    Args:
        content: The text content to append.
        filename: The name of the file to write to (default is 'notes.txt').
        directory: Optional. The path to the directory (e.g., 'Desktop', 'Documents/MyFiles', '~/my_folder').
                   Paths are resolved relative to your home directory (~).
                   For security, paths must be within your home directory.
    """
    try:
        target_dir = _resolve_directory_path(directory)
        full_path = os.path.join(target_dir, filename)

        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content + "\n")

        return f"Content appended to '{filename}' in '{target_dir}'."

    except ValueError as ve:
        return f"Error appending to file: {ve}"
    except Exception as e:
        return f"Error appending to file '{filename}' in '{target_dir}': {e}" # type: ignore

@mcp.tool()
def read_notes(filename: str = "notes.txt", directory: str = None) -> str: # type: ignore
    """
    Reads and returns the contents of the specified file from the specified directory.
    If no directory is specified, it defaults to a predefined storage location.

    Args:
        filename: The name of the file to read (default is 'notes.txt').
        directory: Optional. The path to the directory (e.g., 'Desktop', 'Documents/MyFiles', '~/my_folder').
                   Paths are resolved relative to your home directory (~).
                   For security, paths must be within your home directory.
    """
    try:
        target_dir = _resolve_directory_path(directory)
        full_path = os.path.join(target_dir, filename)

        with open(full_path, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found."
    except FileNotFoundError:
        return f"No file named '{filename}' found in '{target_dir}'." # type: ignore
    except ValueError as ve:
        return f"Error reading file: {ve}"
    except Exception as e:
        return f"Error reading file '{filename}' in '{target_dir}': {e}" # type: ignore

# This tool is now primarily for debugging or confirming paths for the user
@mcp.tool()
def get_resolved_path(filename: str = "default_file.txt", directory: str = None) -> str: # type: ignore
    """
    Returns the full absolute path where a file would be stored given the filename and optional directory.
    Useful for confirming the target path before creating/modifying files.
    """
    try:
        target_dir = _resolve_directory_path(directory)
        return os.path.join(target_dir, filename)
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Error resolving path: {e}"
def main():
    # Optional: change host/port if you want it remotely accessible
    mcp.run()
    # mcp.run(host="0.0.0.0", port=8081)

if __name__ == "__main__":
    main()

