from pathlib import Path
from cli_veripy.cli_args import CLIArguments, ExistingPath
import string

def ListStrFactory(valid_chars:str = string.ascii_letters + '_ ', delimiter:str = ','):
    valid_chars += delimiter
    class ListStr(list):
        def __init__(self, value:str):
            for c in value:
                if c not in valid_chars:
                    raise TypeError(f"List argument must contain valid characters.  Invalid character found '{c}'.", c)
            super().__init__(value.split(delimiter))
    return ListStr

if __name__ == "__main__":
    args:CLIArguments = CLIArguments(
        valid_pargs=[Path, str],
        pargs_names=["package-directory", "package-name"],
        valid_flags={
            "no-requirements", "no-deps", "git-ignore", "tests",
            "testing", "no-readme", "utils-folder", "core-folder",
            "examples", "docs", "documentation", "manifest", "force-yes",
            "force-y", "create-project-directory"
        },
        valid_kwargs={
            "version":str, "build-tool":str, "python-version":str,
            "author":str, "license":str, "license-year":int,
            "license-path":ExistingPath, "sub-modules":ListStrFactory()
        },
        required_kwargs=["author"],
        exit_on_invalid=True,
        description="A command line tool for initializing new python projects."
    )

    args["version"] = args["version"] if args["version"] else "0.0.0-ALPHA1"
    args["build-tool"] = args["build-tool"] if args["build-tool"] else "setuptools"
    args["python-version"] = args["python-version"] if args["python-version"] else ">=3.10"
    force_yes = args["force-yes"] or args["force-y"]