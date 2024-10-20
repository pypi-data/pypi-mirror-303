from .decorator import command
from .runner import execute


def ucli():
    """ 
    The main function that executes when the library
    is run from the terminal.
    
        ```bash
        ucli path.to.your.function --help
        ```
    """
    
    from sys import argv
    execute(argv[1], argv[2:])
