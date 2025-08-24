# mcp-course

## Running the MCP Demo Project (class5/demo-mcp-server)

This project demonstrates MCP server and client interaction, including LLM integration. Dependencies are managed with [uv](https://github.com/astral-sh/uv).

### Setup

1. **Install uv** (if not already installed):

    ```sh
    pip install uv
    ```

2. **Install dependencies**:

    ```sh
    cd class5/demo-mcp-server
    uv pip install -r pyproject.toml
    ```

3. **Set up environment variables**:

    - Copy `.env.example` to `.env` and fill in required values (e.g., `GITHUB_TOKEN` for Azure LLM).

4. **Run the client**:

    ```sh
    python client.py
    ```

### Project Structure

- `server.py`: MCP server exposing calculator tools and greeting resource.
- `client.py`: MCP client that lists tools/resources and interacts with an LLM.
- `calculator.py`: Implements calculator logic.
- `.env`: Environment variables for secrets/tokens.
- `pyproject.toml`: Project dependencies.

### Notes

- Ensure MCP is installed and available in your environment.
- The client uses Azure LLM; set `GITHUB_TOKEN` in your `.env`.
- For more details, see [MCP Documentation](https://github.com/microsoft/mcp-for-beginners).
