from typing import Callable, TypeVar

__T = TypeVar("__T", bound=Callable[..., ...])


def native(func: __T) -> __T:
    """
    Force the compilation of this function to native code, bypassing Pylang's automatic decision.

    When using this decorator, Pylang will attempt to compile the target function into native code
    (e.g., C or Cython). This can potentially improve performance significantly, but may also lead
    to the following issues:

    - **Behavior changes**: Native compilation may alter certain Python language features or behaviors,
     meaning the compiled function might behave differently from the original Python function.
    - **Runtime errors**: In some cases, the compilation process may fail, resulting in runtime errors
     or undefined behavior.
    - **Fallback mechanism**: If the native compilation fails, Pylang will automatically fall back to
     interpreting the function as a regular Python function.

    **Note**:
    - Ensure that the logic of the function is safe to compile into native code before using `@native`.
    - Additional testing may be required to verify that the behavior of the compiled function matches
     expectations.

    Example:
       @native
       def compute_heavy_task(x, y):
           # Complex computation logic
           return x ** y
    """
    return func


def pure(func: __T) -> __T:
    """
    Mark this function as a pure function, allowing Pylang to precompute its result.

    A pure function is one that always returns the same output for the same input and does not depend on
    or modify external state. By using the `@pure` decorator, Pylang can optimize the function by potentially
    precomputing its result at compile time, eliminating the need to call it at runtime.

    **Note**:
    - Pylang **may** precompute the result of a pure function, but this is not guaranteed. In some cases,
      Pylang may still retain the function call.
    - Make sure that the function truly adheres to the definition of a pure function, i.e., no side effects
      and consistent return values for the same inputs.
    - Using `@pure` on functions that are not pure may lead to incorrect optimizations.

    Example:
        @pure
        def add(a, b):
            return a + b
    """
    return func
