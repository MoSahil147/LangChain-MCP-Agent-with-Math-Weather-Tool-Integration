from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """_summary_
    Get the weather location
    """
    return f"The weather of {location} is rainy"

## It sets up an HTTP API where requests and responses are streamed instead of sent all at once.
if __name__ == "__main__":
    mcp.run(transport="streamable-http")