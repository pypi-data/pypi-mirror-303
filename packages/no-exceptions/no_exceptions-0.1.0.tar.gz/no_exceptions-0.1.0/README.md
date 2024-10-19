# `no_exceptions`

Errors as values for Python. A more functional alternative to `try-except` blocks, offering less indented code and a
chainable API.

- Do you hate exceptions?
- Do you hate the extra indentation they bring?
- Do you hate the convoluted flow of control they seed?
- Do you hate APIs that throw exceptions in not-really-erroneous cases (like `ZeroDivisionError`, `KeyError`,
`IndexError`, `StopIteration`)?

Use this package to switch from this:

```python
def some_func() -> float:
    ...
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0.0
```

to this:

```python
from no_exceptions import try_expecting

def some_func() -> float:
    ...
    return try_expecting(lambda: numerator / denominator, ZeroDivisionError).unwrap_or(0.0)
```
