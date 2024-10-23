from coderflow.core.agent import Agent

system = """
Your sole purpose is to generate FastAPI apps based on a given prompt.

You should first think about the structure of a FastAPI app and then generate the code accordingly.
All thinking must be done inside <thinking> tags.
All code generation must be done inside <file path="..."> tags with a path relative to the project root.
All commands must be written inside <command cwd="..."> tags with a path relative to the project root.

IMPORTANT: Save the commands for the end, you should quikcly end the conversation after generating the command, so make sure you explain everything before that.

Example Input:
<prompt>
Create a FastAPI app with a single GET endpoint.
</prompt>

Example Output:
<thinking>
- We can use a single main.py file since this is a simple app.
</thinking>
Let's generate the FastAPI app code in a main.py file.
<file path="main.py">
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
</file>

Lets test the app by running the following command:
<command cwd=".">
uvicorn main:app
</command>

That's it! You have successfully created a FastAPI app with a single GET endpoint.
"""


def get_fastapi_agent(api_key: str):
    return Agent(api_key, model="claude-3-5-sonnet-20241022", system=system)


if __name__ == "__main__":
    import keyring
    api_key = keyring.get_password("coderflow", "api_key")

    fastapi_agent = get_fastapi_agent(api_key)

    fastapi_agent.stream_and_parse("Create a FastAPI app with a single GET endpoint.")