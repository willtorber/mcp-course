"""
Doc: https://github.com/microsoft/mcp-for-beginners/blob/main/03-GettingStarted/05-sse-server/README.md

Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python. 
It is production-ready, and gives you the following: A lightweight, low-complexity HTTP web framework. 
WebSocket support. In-process background tasks. Startup and shutdown events.

"""

from mcp.server.fastmcp import FastMCP
from calculator import Calculator
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP

calc = Calculator()

# Create an MCP server
mcp = FastMCP("My App")

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

# Tools
@mcp.tool()
def add(a: float, b: float) -> str:
    return calc.add(a, b)

@mcp.tool()
def subtract(a: float, b: float) -> str:
    return calc.subtract(a, b)

@mcp.tool()
def multiply(a: float, b: float) -> str:
    return calc.multiply(a, b)

@mcp.tool()
def divide(a: float, b: float) -> str:
    return calc.divide(a, b)

@mcp.tool()
def power(base: float, exponent: float) -> str:
    return calc.power(base, exponent)

@mcp.tool()
def square_root(number: float) -> str:
    return calc.square_root(number)

@mcp.tool()
def modulus(a: float, b: float) -> str:
    return calc.modulus(a, b)

@mcp.tool()
def absolute(number: float) -> str:
    return calc.absolute(number)

@mcp.tool()
def help() -> str:
    return calc.help()

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Main execution block - this is required to run the server
if __name__ == "__main__":
    mcp.run()
