from os import mkdir, path as os_path
from typer import Exit
from rich import print
from typing_extensions import Optional

class make:
    @staticmethod
    def absjoiner(paths: list = None):
        try:
            if paths is not None and type(paths) == list:
                fullpath: str = ""
                for path in paths:
                    if type(path) == str:
                        fullpath = os_path.abspath(os_path.join(fullpath, path))
                return fullpath
        except Exception as err:
            print(f"[bold white][red]{err}[/red] Sağlanan dosya yolları hatalı! Lütfen girdiğiniz dosya yollarını tekrar gözden geçiriniz.[/bold white]")
            raise Exit()

    @staticmethod
    def file(name: str = None, content: Optional[str] = None):
        try:
            with open(name, "w", encoding="utf-8") as f:
                if content is not None:
                    f.write(content)
                f.close()
        except Exception as err:
            print(f"[bold white][red]{err}[/red] Yeni bir Dosya oluşturulurken bir sorun meydana geldi![/bold white]")
            raise Exit()
        
    @staticmethod
    def dir(name: str = None):
        try:
            mkdir(name)
        except Exception as err:
            print(f"[bold white][red]{err}[/red] Yeni bir Klasör oluşturulurken bir sorun meydana geldi![/bold white]")
            raise Exit()