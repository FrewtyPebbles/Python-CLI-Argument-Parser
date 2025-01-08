from pathlib import Path
from cli_veripy.cli_args import CLIArguments, ExistingPath, CLIArgument
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
            "no-requirements", "no-deps", "git-ignore",
            CLIArgument("tests", description="Creates a tests directory in the root of the package."),
            "testing", "no-readme", "utils-folder", "core-folder",
            "examples", "docs", "documentation", "manifest", "force-yes",
            "force-y", "create-project-directory"
        },
        valid_kwargs={
            "version":CLIArgument("Version", str,
                validation_function=lambda arg:
                    not any(letter in arg.lower() for letter in string.ascii_lowercase) or
                    any(word in arg.lower() for word in [
                        "development","dev", "d", "version", "ver", "v",
                        "alpha", "a", "beta", "b", "testing", "test", "t",
                        "release","rel", "r"
                    ]),
                description="The starting version string of your package.",
                long_description=f"""Common versioning tokens such as "development", "alpha", "beta", "release", "test", etc. are valid in the string.  The characters "a-z", "A-Z" and "._- " are also allowed.  This will be the version that appears in your build tools and config files."""
            ),
            "build-tool":str, "python-version":str,
            "author":str,
            "license":CLIArgument("License", str, validation_function=lambda arg: arg in {"MIT"},
                description="The Licence under which your package will be distributed."                      
            ),
            "license-year":int,
            "license-path":ExistingPath, "sub-modules":ListStrFactory()
        },
        required_kwargs=["author"],
        exit_on_invalid=True,
        description="A command line tool for initializing new python projects.",
        help_menu=False
    )

    args["version"] = args["version"] if args["version"] else "0.0.0-ALPHA1"
    args["build-tool"] = args["build-tool"] if args["build-tool"] else "setuptools"
    args["python-version"] = args["python-version"] if args["python-version"] else ">=3.10"
    force_yes = args["force-yes"] or args["force-y"]

    print(args[0], args[1], args["version"], args["force-y"])