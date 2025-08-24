"""
Doc: https://github.com/microsoft/mcp-for-beginners/blob/main/03-GettingStarted/03-llm-client/README.md

Adding an LLM sounds simple, but will we actually do this?

Here's how the client will interact with the server:

1. Establish connection with server.
2. List capabilities, prompts, resources and tools, and save down their schema.
3. Add an LLM and pass the saved capabilities and their schema in a format the LLM understands.
4. Handle a user prompt by passing it to the LLM together with the tools listed by the client.
"""

import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
# llm
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import json

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Load GITHUB_TOKEN env
            load_dotenv()

            # Initialize the connection
            await session.initialize()

            # List available tools
            functions = []
            tools = await session.list_tools()
            print("LISTING TOOLS")
            for tool in tools.tools:
                print("Tool: ", tool.name)
                print("Tool", tool.inputSchema["properties"])
                functions.append(convert_to_llm_tool(tool))

            prompt = "Add 15 to 37"

            # ask LLM what tools to call, if any
            functions_to_call = call_llm(prompt, functions)

            # call suggested functions
            for f in functions_to_call:
                result = await session.call_tool(f["name"], arguments=f["args"])
                print("TOOLS result: ", result.content)



def convert_to_llm_tool(tool):
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
            }
        }
    }

    return tool_schema

# llm
def call_llm(prompt, functions):
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.inference.ai.azure.com"

    model_name = "gpt-4o"

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    print("CALLING LLM")
    response = client.complete(
        messages=[
            {
            "role": "system",
            "content": "You are a helpful assistant.",
            },
            {
            "role": "user",
            "content": prompt,
            },
        ],
        model=model_name,
        tools = functions,
        # Optional parameters
        temperature=1.,
        max_tokens=1000,
        top_p=1.    
    )

    response_message = response.choices[0].message
    
    functions_to_call = []

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            print("TOOL: ", tool_call)
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            functions_to_call.append({ "name": name, "args": args })

    return functions_to_call

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

