import pytest

from runtypes import *


def test_creation():
    # Create common type to be used
    MyType = typedtuple("MyType", [("a", int), ("b", str), ("c", bool)])

    # This should work
    m_inst = MyType(1, "Hello World", False)
    assert repr(m_inst) == "MyType(a=1, b='Hello World', c=False)"
    assert m_inst.a == 1
    assert m_inst.b == "Hello World"
    assert m_inst.c == False

    # This should not work
    with pytest.raises(TypeError):
        m_inst = MyType("Hello World", 1, False)
