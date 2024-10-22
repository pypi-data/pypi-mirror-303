"""
Functional programming tools
"""

import inspect
from functools import lru_cache, wraps
from typing import Any, Callable, List, Protocol

__all__ = ['compose', 'pipe']


class ComposeProtocol(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

    def get_intermediate_results(self) -> List[Any]: ...


class PipelineError(Exception):
    """Custom exception for pipeline errors."""


@lru_cache(maxsize=None)
def get_func_signature(func: Callable) -> inspect.Signature:
    """Cache and return the signature of a function."""
    return inspect.signature(func)


def should_unpack(input_value: Any, func: Callable) -> bool:
    """Determine whether the input value should be unpacked for the given function."""
    if not isinstance(input_value, tuple):
        return False

    sig = get_func_signature(func)
    params = list(sig.parameters.values())

    # If there's a *args parameter, we should always unpack
    if any(param.kind == inspect.Parameter.VAR_POSITIONAL for param in params):
        return True

    # Count the number of non-default parameters
    non_default_params = sum(
        1 for param in params if param.default == inspect.Parameter.empty
    )

    # If the number of items in the tuple matches the number of non-default parameters,
    # or if there are more items than parameters (extra will go to *args if present),
    # we should unpack
    return len(input_value) == non_default_params or len(input_value) > len(params)


def compose(*funcs: Callable) -> ComposeProtocol:
    """
    创建一个复合函数，将多个函数串联起来，依次执行。

    Parameters
    ----------
    - `*funcs` : Callable
        - 要串联的函数列表

    Returns
    ----------
    - `ComposeProtocol`
        - 一个管道执行函数
        - 该函数可以像普通函数一样调用，并返回最终结果
        - 该函数还具有 `get_intermediate_results` 方法，可以获取所有中间结果

    Raises
    ----------
    - `PipelineError`
        - _description_

    Example:
    ----------
        >>> def double(x):
        ...     return x * 2
        >>> def add_one(x):
        ...     return x + 1
        >>> pipe = make_pipe(double, add_one)
        >>> result = pipe(3)
        >>> print(result)
        7
        >>> print(pipe.get_intermediate_results())
        [6, 7]
    """

    if not funcs:
        return lambda x: x  # 返回恒等函数

    @wraps(funcs[0])
    def pipeline(*args: Any) -> Any:
        def execute():
            current_value = args
            for i, func in enumerate(funcs):
                try:
                    if i == 0:
                        result = func(*current_value)
                    else:
                        result = (
                            func(*current_value)
                            if should_unpack(current_value, func)
                            else func(current_value)
                        )
                    yield result
                    current_value = result
                except Exception as e:
                    raise PipelineError(
                        f"Error in function '{func.__name__}' at step {i+1}: {str(e)}"
                    ) from e

        pipeline.intermediate_results = list(execute())
        return pipeline.intermediate_results[-1]

    def get_intermediate_results() -> List[Any]:
        return getattr(pipeline, 'intermediate_results', [])

    pipeline.get_intermediate_results = get_intermediate_results
    return pipeline


def pipe(inputs: Any, *funcs: Callable) -> Any:
    """
    创建一个管道函数，将多个函数串联起来，依次执行。

    Parameters
    ----------
    - `inputs` : Any
        - 要传递给第一个函数的输入值
    - `*funcs` : Callable
        - 要串联的函数列表f

    Returns
    ----------
    - `Any`: 执行结果
    """
    if not funcs:
        return inputs

    composed = compose(*funcs)
    return composed(inputs)
