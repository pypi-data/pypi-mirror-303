from sys import argv 
from typing import Callable

from .runner import execute


def command(func: Callable):
    """
    Command Decorator
    -----------------
    
    Use by putting this on top of any function.
        ```python
        @command
        def myfunc(x, y = 56):
            ...
        ```
    """
    
    if "--upycli.debug" in argv:
        print(f"Debug: Arguments `{argv}`")
        
    if func.__name__ in argv:
        execute(func, argv[(3 if argv == "python" else 2):])
        exit(0)
    
    return func
