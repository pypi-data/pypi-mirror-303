import typing
import collections.abc

from runtypes.runtype import RunType, _assert, _assert_istype, _assert_isinstance

# Any is the most basic type and is used by other types, hence defined here
Any = RunType("Any", lambda value: value)


def _union_check(value: typing.Any, *value_types: type) -> None:
    # Make sure the value is an instance of one of the types
    _assert_isinstance(value, tuple(value_types))


def _optional_cast(value: typing.Any, optional_type: type) -> typing.Optional[typing.Any]:
    # If the value is not defined, return None
    if value is None:
        return None

    # Cast the value to the right type
    return optional_type(value)


def _optional_check(value: typing.Any, optional_type: type) -> None:
    # If the value is defined, make sure it is the right type
    if value is not None:
        _assert_isinstance(value, optional_type)


def _literal_check(value: typing.Any, *literal_values: typing.Any) -> None:
    # Make sure value exists
    _assert(value in literal_values, f"Value is not one of {literal_values!r}")


def _float_cast(value: typing.Any) -> float:
    # Cast to float
    return float(value)


def _float_check(value: typing.Any) -> None:
    # Make sure the value is of type float
    _assert_istype(value, float)


def _integer_cast(value: typing.Any) -> int:
    # Cast to int
    return int(value)


def _integer_check(value: typing.Any) -> None:
    # Make sure the value is of type int
    _assert_istype(value, int)


def _boolean_cast(value: typing.Any) -> bool:
    # Cast to bool
    return bool(value)


def _boolean_check(value: typing.Any) -> None:
    # Make sure the value is of type bool
    _assert_istype(value, bool)


def _string_cast(value: typing.Any) -> str:
    # Cast to str
    return str(value)


def _string_check(value: typing.Any) -> None:
    # Make sure the value is an instance of a string
    _assert_istype(value, str)


def _bytestring_cast(value: typing.Any) -> bytes:
    # Cast to bytes
    return bytes(value)


def _bytestring_check(value: typing.Any) -> None:
    # Make sure the value is an instance of bytes
    _assert_isinstance(value, (bytes, bytearray))


def _list_cast(value: typing.Any, item_type: type) -> typing.List[typing.Any]:
    # Make sure value is a list
    _assert_isinstance(value, collections.abc.Sequence)

    # Loop over value and cast items
    return [item_type(item) for item in value]


def _list_check(value: typing.Any, item_type: type) -> None:
    # Make sure value is a list
    _assert_isinstance(value, list)

    # Loop over value and check items
    for item in value:
        _assert_isinstance(item, item_type)


def _dict_cast(value: typing.Any, key_type: type, value_type: type) -> typing.Dict[typing.Any, typing.Any]:
    # Make sure value is a dictionary
    _assert_isinstance(value, collections.abc.Mapping)

    # Loop over value and cast items
    return {key_type(_key): value_type(_value) for _key, _value in value.items()}


def _dict_check(value: typing.Any, key_type: type, value_type: type) -> None:
    # Make sure value is a dictionary
    _assert_isinstance(value, dict)

    # Loop over value and check items
    for _key, _value in value.items():
        # Check the key and value types
        _assert_isinstance(_key, key_type)
        _assert_isinstance(_value, value_type)


def _tuple_cast(value: typing.Any, *item_types: type) -> typing.Tuple[typing.Any, ...]:
    # Make sure value is a tuple
    _assert_isinstance(value, collections.abc.Sequence)

    # If types do not exist, return
    if not item_types:
        return tuple(value)

    # Make sure value is of length
    _assert(len(value) == len(item_types), "Value length does not match types")

    # Check all item types
    return tuple(item_type(item) for item, item_type in zip(value, item_types))


def _tuple_check(value: typing.Any, *item_types: type) -> None:
    # Make sure value is a tuple
    _assert_isinstance(value, tuple)

    # If types do not exist, return
    if not item_types:
        return

    # Make sure value is of length
    _assert(len(value) == len(item_types), "Value length does not match types")

    # Check all item types
    for item, item_type in zip(value, item_types):
        # Check the item type
        _assert_isinstance(item, item_type)


# Generic types
Union = RunType("Union", checker=_union_check)
Literal = RunType("Literal", checker=_literal_check)
Optional = RunType("Optional", caster=_optional_cast, checker=_optional_check)

# Built-in types
Text = RunType("Text", caster=_string_cast, checker=_string_check)
AnyStr = RunType("AnyStr", caster=_string_cast, checker=_string_check)
ByteString = RunType("ByteString", caster=_bytestring_cast, checker=_bytestring_check)

# Built-in extension types
Float = RunType("Float", caster=_float_cast, checker=_float_check)
Integer = RunType("Integer", caster=_integer_cast, checker=_integer_check)
Boolean = RunType("Boolean", caster=_boolean_cast, checker=_boolean_check)

# Container types
List = RunType("List", caster=_list_cast, checker=_list_check)
Dict = RunType("Dict", caster=_dict_cast, checker=_dict_check)
Tuple = RunType("Tuple", caster=_tuple_cast, checker=_tuple_check)
