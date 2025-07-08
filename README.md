# Claude MCP Tools: LocalNotes and Prompt

This document explains two MCP (Machine Callable Plugin) servers implemented in Python using `FastMCP` from the `mcp` package. These allow natural language tools to be registered for use by Claude or other AI agents.

---
### LocalNotes: File Management Tools and prompts generator

* Create a new file with content
* Append notes to an existing file
* Read content from a file
* Get full path resolution

### Tools

| Tool Name           | Description                                              |
| ------------------- | -------------------------------------------------------- |
| `create_new_file`   | Create a file with specified name and content            |
| `add_note_to_file`  | Append a note to an existing file (default: `notes.txt`) |
| `read_notes`        | Read content of a specified file                         |
| `get_resolved_path` | Return full absolute file path                           |



This MCP server defines prompt-generating tools. These return text prompts suitable for LLMs to execute indirectly.

### Prompt Tools

| Tool Name                          | Description                                    |
| ---------------------------------- | ---------------------------------------------- |
| `get_prompt`                       | Generate a generic topic analysis prompt       |
| `write_detailed_historical_report` | Generate a structured historical report prompt |
| `prompt_create_file`               | Prompt to create a file with given content     |
| `prompt_append_to_file`            | Prompt to append content to a file             |
| `prompt_read_file`                 | Prompt to read a file                          |




## Requirements

* Python 3.10+
* `uv` package manager (fast Python runner)
* `mcp[cli]` Python package

---

## Optional Testing with CLI
mcp install local.py

---
### Add it to package manager (github)
uploading code to github
uvx --from git+https://github.com/Gagan793/mcpserver.git mcp-server 

### Claude Usage 
{
  "mcpServers": {
    "localfiles": {
      "command": "uvx",
      "args": [
        "--from",
        "https://github.com/Gagan793/localfiles_mcp.git",
        "mcp-server"
      ]
    }
  }
}

