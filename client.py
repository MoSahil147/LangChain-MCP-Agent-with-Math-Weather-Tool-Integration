## Will make somtheing here that will be able to nteract with mathserver.py and weather.py

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
##rom langchain_core import messages

from dotenv import load_dotenv
load_dotenv()

## async stands for asynchronous, and it’s used in programming to allow tasks to run without blocking other tasks.
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  ## Ensuring correct absolute path
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  ## Fixed to match weather.py port
                "transport": "streamable-http",
            },
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    print("Getting tools...")
    tools = await client.get_tools()
    print("Tools loaded:", [tool.name for tool in tools])

    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_react_agent(model, tools)

    print("Invoking agent...")
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (3+8)*5?"}]}
    )

    print("Math Response:", math_response['messages'][-1].content)
    
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in Tokyo?"}]}
    )
    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())