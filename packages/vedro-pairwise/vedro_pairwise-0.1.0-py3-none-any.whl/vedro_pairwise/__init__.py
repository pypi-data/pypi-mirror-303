from typing import Any, Callable, Iterable

from allpairspy import AllPairs
from vedro import params

__version__ = "0.1.0"
__all__ = ("params_pairwise", "ParamsPairwise",)


class ParamsPairwise:
    """
    A decorator for parameterized testing that generates pairwise combinations of the provided
    test parameters to create optimized test scenarios, ensuring that all possible pairs of
    parameters are tested while reducing the total number of combinations.

    Parameters:
        *args: Positional arguments representing the test parameters, which must be iterable.
        **kwargs: Keyword arguments representing the test parameters, which must be iterable.

    Raises:
        ValueError: If fewer than two iterable arguments are provided.
    """

    def __init__(self, *args: Iterable[Any], **kwargs: Iterable[Any]) -> None:
        self._args = args
        self._kwargs = kwargs

    def __call__(self, fn: Callable[..., None]) -> Callable[..., None]:
        iterables = list(self._args) + list(self._kwargs.values())
        if len(iterables) < 2:
            raise ValueError("At least two iterable arguments (positional or keyword) "
                             "must be provided for pairwise testing")
        combinations = list(AllPairs(iterables))
        for combo in reversed(combinations):
            fn = params(*combo)(fn)
        return fn


params_pairwise = ParamsPairwise
