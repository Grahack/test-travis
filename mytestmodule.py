"""Fake module to test tests."""

def test_proc(x):
    """Fake procedure to test doctests.

    >>> test_proc(42)
    43

    """
    return x

import doctest
doctest.testmod()
