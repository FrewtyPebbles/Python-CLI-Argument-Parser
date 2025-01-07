from cli_args import CLIArguments, CLIError, ExistingPath
import sys
from pathlib import Path

cli_args = CLIArguments(
    valid_pargs=[ExistingPath, Path],
    valid_kwargs={
        "project_name":str
    },
    required_kwargs=["project_name"],
    minimum_pargs=1,
    exit_on_invalid=True
)

print(f"""
Project Name: {cli_args["project_name"]}
Root Path:    {cli_args[0]}
arg1:         {cli_args[1].exists()}
""")
