import keyring
import typer
from coderflow.agents.fastapi import get_fastapi_agent
from coderflow.agents.react import get_react_agent

app = typer.Typer()

SERVICE_NAME = "coderflow"

def ensure_api_key():
    """
    Middleware to ensure an API key is set before executing any command.
    Prompts the user to set the API key if not found.
    """
    api_key = keyring.get_password(SERVICE_NAME, "api_key")
    if not api_key:
        typer.echo("No API key found. Please enter your API key:")
        api_key = typer.prompt("API Key")
        keyring.set_password(SERVICE_NAME, "api_key", api_key)
        typer.echo("API key has been set successfully.")
    return api_key

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Middleware to execute before any command.
    Ensures an API key is available.
    """
    if ctx.invoked_subcommand is not None:
        # Run the middleware to check the API key
        ensure_api_key()


@app.command()
def update_api_key(new_api_key: str = typer.Option(..., prompt=True, help="The new API key")):
    """
    Update the API key to a new value.
    """
    keyring.set_password(SERVICE_NAME, "api_key", new_api_key)
    typer.echo("API key has been updated successfully.")


@app.command()
def fastapi(prompt: str):
    """
    Generate a FastAPI app based on a given prompt.
    """
    api_key = ensure_api_key()
    fastapi_agent = get_fastapi_agent(api_key)
    fastapi_agent.stream_and_parse(prompt)


@app.command()
def react(prompt: str):
    """
    Generate a React app based on a given prompt.
    """
    api_key = ensure_api_key()
    react_agent = get_react_agent(api_key)
    react_agent.stream_and_parse(prompt)


if __name__ == "__main__":
    app()
