import pytest

from runtypes import *


def test_no_hints():

    @typecheck
    def my_function(a, b, c, d):
        return (a, b, c, d)

    assert my_function(1, 2, 3, 4) == (1, 2, 3, 4)


def test_some_hints():

    @typecheck
    def my_function(a, b: str, c, d):
        return (a, b, c, d)

    assert my_function(1, "2", 3, 4) == (1, "2", 3, 4)

    with pytest.raises(TypeError):
        my_function(1, 2, 3, 4)


def test_default_values():

    @typecheck
    def my_function(a, b: str, c, d: int = 1):
        return (a, b, c, d)

    assert my_function(1, "2", 3) == (1, "2", 3, 1)

    with pytest.raises(TypeError):
        my_function(1, "2", 3, "4")


def test_bad_default_values():

    @typecheck
    def my_function(a, b: str, c, d: int = "1"):
        return (a, b, c, d)

    assert my_function(1, "2", 3, 1) == (1, "2", 3, 1)

    with pytest.raises(TypeError):
        my_function(1, "2", 3)


def test_kwargs():

    @typecheck
    def my_function(a, b: str, c=None, d: int = "1"):
        return (a, b, c, d)

    assert my_function(1, "2", 3, d=1) == (1, "2", 3, 1)

    with pytest.raises(TypeError):
        my_function(1, "2", d="A")


def test_cast():

    class MyClass:
        pass

    @typecast
    def my_function(a, b: str, c: int, d: Optional[Boolean], e: MyClass):
        return (a, b, c, d, e)

    x = MyClass()

    assert my_function(1, 2, 3, 4, x) == (1, "2", 3, True, x)

    with pytest.raises(TypeError):
        my_function(1, 2, object(), object(), x)

    with pytest.raises(TypeError):
        my_function(1, 2, 3, 4, 5)
