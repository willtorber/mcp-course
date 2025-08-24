# mcp-course

## Debugging an SSE Server with Inspector

### 1- Running the inspector
To run the inspector, you first must have an SSE server running, so let's do that next:
```
uvicorn server:app
```
> Note how we use the executable uvicorn that's installed when we typed pip install "mcp[cli]". Typing server:app means we're trying to run a file server.py and for it to have a Starlette instance called app.

### 2- Run the inspector
> Run this in a separate terminal window than the server is running in. Also note, you need to adjust the below command to fit the URL where your server runs.

```
npx @modelcontextprotocol/inspector mcp run server.py
```