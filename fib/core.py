"""Core Fibonacci logic."""

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    Parameters
    ----------
    n: int
        Non-negative index of the Fibonacci sequence.

    Returns
    -------
    int
        The Fibonacci number at position n.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
