from subprocess import run as run_subprocess
from typing_extensions import Optional
from rich import print

def runcmd(command: str, title: Optional[str], cwd=None):
    if title:
        print(f"     [bold white][green]running...[/green] {title}[/bold white]")
    run_subprocess(command, shell=True, text=True, cwd=cwd, capture_output=True)