from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """_summary_
    Add two numbers
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """_summary_
    Multiply two numbers
    """
    return a * b

## undestand the below code as people do write it but fail to undertsand this
## transport="stdio" tells the program to send and receive data using standard input/output (stdin/stdout) instead of other methods like HTTP, sockets, or files.
if __name__ == "__main__":
    mcp.run(transport="stdio")