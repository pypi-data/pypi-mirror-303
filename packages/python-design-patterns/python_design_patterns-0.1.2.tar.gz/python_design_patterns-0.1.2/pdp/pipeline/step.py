""" This module contains the Step class, which is used to represent a step in a pipeline. """

from typing import Any, Callable, List


class Step:
    """Step class for the pipeline module"""

    def __init__(self, name: str, func: Callable[..., Any]):
        self.name = name
        self.func = func

    def get_args(self) -> List[str]:
        """Get the arguments of the function

        :return: the arguments of the function
        :rtype: Any
        """
        return list(self.func.__code__.co_varnames[: self.func.__code__.co_argcount])

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call the function with the given arguments and keyword arguments

        :param args: positional arguments
        :type args: Any
        :param kwargs: keyword arguments
        :type kwargs: Any

        :return: the result of the function
        :rtype: Any
        """
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"{self.name}, {self.func}"

    def __str__(self):
        return self.__repr__()
