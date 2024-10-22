#!/usr/bin/env python
from typing import Optional
from rich import print
from typing_extensions import Annotated
from typer import run, Exit, Argument, Option
from cli.maker import make
from cli.repo import repository
from cli.template import template

__version__ = "0.1.9"

# Yeni bir depo oluşturmak için kullanılır.
def create_new_repo(repo: str = None, token: str = None):
    # depo belirtilmiş ve metin olarak belirtilmiş ise...
    if repo is not None and type(repo) == str:
        print("     [green bold]Creating a lesson...[/green bold]")

        # Yeni bir klasör oluşturuyoruz ve aynı isim ile yeni bir github deposu oluşturuyoruz.
        repository.create(repo, token)

        try:
            template(repo)
        except Exception as err:
            print(f"[bold white][red]{err}[/red] Template dosyaları oluşturulurken bir sorun meydana geldi![/bold white]")
            raise Exit()
            
        print(f"     [bold green]Successfully created[bold green] [bold white]{make.absjoiner([repo])}[/bold white]")


def main(
    new: Annotated[Optional[str], Argument(help="Yeni bir depo oluşturmak için depo adını belirtiniz.")] = None,
    version: Annotated[bool, Option(help="Kullanmakta olduğunuz on-on sürümünü gösterir.")] = False,
    token: Annotated[Optional[str], Option(help="Özel bir token belirtiniz.")] = None
    ):
    
    if version:
        print(__version__)
        raise Exit()

    if new is not None:
        create_new_repo(new, token)
    else:
        print(f"[bold red]Please provide a valid [white]lesson name[/white][/bold red]")
    

def exec():
    run(main)

if __name__ == "__main__":
    exec()