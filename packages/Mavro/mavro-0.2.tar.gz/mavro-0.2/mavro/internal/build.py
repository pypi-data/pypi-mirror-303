import os
import subprocess
import sys
from typing import Callable

from ..parser.lens import LensParser
from ..parser.lines import LineParser
from ..internal.driver import create_temporary_file_from_lens

def build(path: str, dist_path: str | None = None, no_delete: bool = False, line_loader: Callable | None = None) -> None:
    with open(path) as file_literal:
        cont: str = file_literal.read()
    lens: LensParser = LensParser(
        cont=cont,
        baseline=LineParser(),
        line_loader=line_loader
    )
    no_delete = no_delete or "--no-delete" in sys.argv
    with create_temporary_file_from_lens(lens, dist_path=dist_path, no_delete=no_delete) as fn:
        result: subprocess.CompletedProcess = subprocess.run(["python.exe", fn], stderr=subprocess.PIPE)
        if result.stderr:
            result.stderr = result.stderr.decode()
            if "--disable-error-handling" in sys.argv:
                print(result.stderr)
                return
            try: info: str = result.stderr.split("\n")[-2].split(":", 1)[1].lstrip()
            except Exception: # NOQA
                info: str = "no error information"
            try: name: str = result.stderr.split("\n")[-2].split(":", 1)[0]
            except Exception: # NOQA
                name: str = ""
            print(f"fatal {name}: \033[31m{info}\033[0m")
def build_from_sys_argv() -> None:
    args: list[str] = sys.argv
    try: args[1]
    except IndexError:
        args.append(".")
    if os.path.exists(args[1]):
        if os.path.isdir(args[1]):
            path: str = f"{args[1].strip("\\/").replace("\\", "/")}/main.mav"
            if os.path.exists(path):
                build(path)
            else:
                print(f"'{path}' does not exist, and cannot be executed.")
        else:
            build(args[1])
    else:
        print(f"'{args[1]}' does not exist, and cannot be executed")
if __name__ == "__main__":
    build_from_sys_argv()