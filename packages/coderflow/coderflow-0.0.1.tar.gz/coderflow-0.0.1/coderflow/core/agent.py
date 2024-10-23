import signal

import anthropic
from coderflow.core.parse import StreamParser

DEFAULT_MODEL = "claude-3-haiku-20240307"
DEFAULT_SYSTEM = "You are a helpful agent."


class Agent:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, system: str = DEFAULT_SYSTEM):
        self.anthropic_client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.system = system
        self.parser = StreamParser()
        # Attach signal handler for SIGINT
        signal.signal(signal.SIGINT, self.signal_handler)

    def stream(self, prompt: str):
        """Streams the response from the Anthropic model."""
        with self.anthropic_client.messages.stream(
            model=self.model,
            max_tokens=4096,
            system=self.system,
            messages=[
                {"role": "user", "content": prompt}
            ]
        ) as stream_response:
            for chunk in stream_response.text_stream:
                yield chunk

    def stream_and_parse(self, prompt: str):
        """Streams the response from the Anthropic model and parses it."""
        for chunk in self.stream(prompt):
            self.parser.parse(chunk)

    def signal_handler(self, sig, frame):
        if self.parser.current_process:
            self.parser.current_process.terminate()
            self.parser.current_process.wait()
            print("\n[red]Subprocess terminated.[/red]")
        else:
            print("\n[red]No subprocess to terminate.[/red]")
