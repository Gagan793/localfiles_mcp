from mcpserver.local import mcp
from mcpserver.prompt import mcpserver
def main():
    # Optional: change host/port if you want it remotely accessible
    mcp.run()
    mcpserver.run()
    # mcp.run(host="0.0.0.0", port=8081)

if __name__ == "__main__":
    main()
