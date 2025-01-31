# cli_veripy

This is a robust CLI arguments verification and management module that I made for use in my own CLI projects.

# Quickstart/Features

 - pargs are positional arguments and can be accessed via `cli_args_instance[some integer index]` or via a key string if a parg name is provided via pargs_names

 - The `CLIArgument` class (not to be confused with `CLIArguments`) can be used instead of types when defining your positional arguments, keyword arguments and flags for extra validation and documentation.

 - If `help_menu` is set to `True` when creating the `CLIArguments`, you can display documentation (if available) for the argument by doing `python program_name.py help:argument_name`.  

 - To require a CLI argument to be an existing file system path, you can set the CLI argument type to `ExistingPath`.  The `CLIArguments` class will then automatically handle any invalid paths.

 - If you wish to have CLI errors handled by `CLIArguments` just set exit_on_invalid to true when `CLIArguments.__init__` is called.