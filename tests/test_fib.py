from app.utils import fib
import pytest

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (10, 55),
    (20, 6765),
])
def test_fib(n, expected):
    assert fib(n) == expected
