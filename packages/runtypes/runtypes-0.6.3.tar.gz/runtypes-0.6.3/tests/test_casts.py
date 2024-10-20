import pytest

from runtypes import *


def test_list_cast():
    assert List[int](["1", 2]) == [1, 2]
    assert not isinstance(["Hello", "World", 42], List[str])
    assert not isinstance(["Hello", 10], List[Text])


def test_dict_cast():
    assert Dict[str, int]({"a": "1"}) == {"a": 1}
    assert isinstance({"hello": "world", "test": "test"}, Dict[Text, Text])
    assert not isinstance({"hello": "world", "test": 42}, Dict[Text, str])
    assert not isinstance({"hello": "world", "test": 42}, Dict[Text, Text])


def test_tuple_cast():
    assert Tuple[int, int]((1, "2")) == (1, 2)
    assert not isinstance((1, "2"), Tuple[int, int])
    assert isinstance((1, 2, 3), Tuple[int, int, int])


def test_schema_cast():
    schema = Schema[{"hello": int, "sub": {"thing": int}}]
    assert schema({"hello": "1", "sub": {"thing": True}}) == {"hello": 1, "sub": {"thing": 1}}
    assert isinstance({"hello": 1, "sub": {"thing": 1}}, schema)
    assert not isinstance({"hello": "1", "sub": {"thing": True}}, schema)


def test_charset_cast():
    assert Charset["HeloWrd "]("Hello World!") == "Hello World"
    assert isinstance("Hello World", Charset["HeloWrd "])
    assert not isinstance("Test", Charset["HeloWrd "])


def test_id_cast():
    assert ID("asdasdasd?") == "asdasdasd"
    assert isinstance("asdasdasd", ID)
    assert not isinstance("asdasdasd?", ID)


def test_binary_cast():
    assert Binary("001011012") == "00101101"
    assert isinstance("00101101", Binary)
    assert not isinstance("001011012", Binary)


def test_decimal_cast():
    assert Decimal("1234F") == "1234"
    assert Decimal("0x1234F") == "01234"
    assert isinstance("1234", Decimal)
    assert not isinstance("0x1234", Decimal)


def test_hexadecimal_cast():
    assert Hexadecimal("badc0ffeZ") == "badc0ffe"
    assert isinstance("badc0ffe", Hexadecimal)
    assert not isinstance("badc0ffeZ", Hexadecimal)
