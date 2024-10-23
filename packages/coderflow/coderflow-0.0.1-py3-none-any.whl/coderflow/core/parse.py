import os
import subprocess
import sys

from rich.console import Console


class StreamParser:
    def __init__(self):
        self.buffer = ""
        self.tag_buffer = ""
        self.in_tag = False
        self.in_thinking = False
        self.in_file = False
        self.in_command = False
        self.file_path = None
        self.file_content = ""
        self.command = None
        self.command_cwd = None
        self.current_process = None
        self.console = Console()

    def _flush_buffer(self):
        # Flush the regular buffer to stdout if not in a special state
        if self.buffer and not (self.in_thinking or self.in_file or self.in_command or self.in_tag):
            sys.stdout.write(self.buffer)
            sys.stdout.flush()
        self.buffer = ""

    def _handle_tag_open(self):
        # Handle the tag opening based on the content of the tag_buffer
        tag_content = self.tag_buffer[1:-1].strip()
        if tag_content.startswith("thinking"):
            self.in_thinking = True
            self.console.print("[green]thinking...[/green]", end="")
        elif tag_content.startswith("file"):
            start = tag_content.find('path="') + 6
            end = tag_content.find('"', start)
            self.file_path = tag_content[start:end]
            self.in_file = True
            self.console.print(f"[yellow]writing file \"{self.file_path}\"...[/yellow]", end="")
        elif tag_content.startswith("command"):
            start = tag_content.find('cwd="') + 5
            end = tag_content.find('"', start)
            self.command_cwd = tag_content[start:end]
            self.in_command = True
            self.command = ""
            self.console.print(f"[cyan]running command in \"{self.command_cwd}\"...[/cyan]", end="")
        self.tag_buffer = ""

    def _handle_tag_close(self):
        # Handle the tag closing based on the content of the tag_buffer
        tag_content = self.tag_buffer[2:-1].strip()
        if self.in_thinking and tag_content == "thinking":
            self.in_thinking = False
            self.console.print("\n[green]done thinking[/green]")
        elif self.in_file and tag_content == "file":
            self.in_file = False
            full_path = os.path.join("output", self.file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w") as f:
                f.write(self.file_content)
            self.console.print(f"\n[yellow]done writing file \"{self.file_path}\"[/yellow]")
            self.file_path = None
            self.file_content = ""
        elif self.in_command and tag_content == "command":
            self.in_command = False
            try:
                self.console.print(f"\n[cyan]running command \"{self.command}\" in \"{self.command_cwd}\"[/cyan]")
                self._run_command_with_handling(self.command, self.command_cwd)
                self.console.print(f"[cyan]done running command.[/cyan]")
            except subprocess.TimeoutExpired:
                self.console.print(f"[red]command timed out.[/red]")
            self.command = None
            self.command_cwd = None
        self.tag_buffer = ""

    def _run_command_with_handling(self, command, cwd):
        # Run a command and handle interrupt signal to stop the process without exiting the program
        self.current_process = subprocess.Popen(
            command, shell=True, cwd=os.path.join("output", cwd),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        try:
            for line in self.current_process.stdout:
                self.console.print(f"[magenta]{line.strip()}[/magenta]")
        except KeyboardInterrupt:
            self.console.print("\n[red]Command interrupted by user[/red]")
            self.current_process.terminate()
            self.current_process.wait()
        finally:
            self.current_process = None

    def parse(self, chunk):
        for char in chunk:
            if char == "<":
                # Start of a tag
                self._flush_buffer()
                self.in_tag = True
                self.tag_buffer = "<"
            elif char == ">" and self.in_tag:
                # End of a tag
                self.tag_buffer += ">"
                self.in_tag = False
                if self.tag_buffer.startswith("</"):
                    self._handle_tag_close()
                else:
                    self._handle_tag_open()
            elif self.in_tag:
                # Inside a tag
                self.tag_buffer += char
            else:
                # Regular text, file content, or command content
                if self.in_file:
                    self.file_content += char
                elif self.in_command:
                    self.command += char
                elif not self.in_thinking:
                    self.buffer += char

        # Flush any remaining buffer
        self._flush_buffer()


if __name__ == "__main__":
    # Simulate parsing a stream of data
    stream_data = [
        'Okay, let`s',
        ' generate',
        ' a',
        ' simple',
        ' "',
        'Hello, World!"',
        ' FastAPI app.',
        '\n\n<thinking',
        '>\n- For',
        ' a basic "',
        'Hello, World!"',
        ' app',
        ', we only',
        ' need a single main',
        '.py file with',
        ' a',
        ' single',
        ' GET',
        ' endpoint.\n-',
        ' The',
        ' endpoint',
        ' will return a simple',
        ' JSON',
        ' response with the "',
        'Hello, World!"',
        ' message.\n</',
        'thinking>\n\n',
        '<file path="main',
        '.py">',
        '\nfrom fastapi import',
        ' FastAPI\n\napp',
        ' = FastAPI()',
        '\n\n@app.',
        'get("/")',
        '\nasync def read_',
        'root():\n    ',
        'return {"message',
        '": "Hello,',
        ' World!"}',
        '\n</file>',
        '\n\nThis',
        ' code',
        ' will',
        ' create a FastAPI',
        ' app with a single',
        ' GET endpoint at the',
        ' root URL',
        ' ',
        '("/"). When',
        ' the endpoint',
        ' is accesse',
        'd, it will return',
        ' a JSON response with',
        ' the message "Hello',
        ', World!".',
        '\n\nYou',
        ' can run this Fast',
        'API app by navig',
        'ating to the project',
        ' directory and running `',
        'uvicorn main',
        ':app --reloa',
        'd`.',
        ' Then',
        ', you can',
        ' visit',
        ' `',
        'http://localhost:',
        '8000/`',
        ' in your web browser',
        ' to see the "',
        'Hello, World!"',
        ' response',
        '.\n',
    ]

    parser = StreamParser()
    for chunk in stream_data:
        parser.parse(chunk)



