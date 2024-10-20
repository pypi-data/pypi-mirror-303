import typing
import collections

from runtypes.runtype import _assert_istype


def TypedTuple(name: str, fields: typing.List[typing.Tuple[str, type]]) -> type:
    # Make sure the name is a string
    _assert_istype(name, str)

    # Create namedtuple classtype
    original_class = collections.namedtuple(name, [key for key, _ in fields])

    # Create the subclass from the original class
    class modified_class(original_class):

        def __new__(cls: type, *args: typing.Any, **kwargs: typing.Any) -> "modified_class":
            # Initialize namedtuple with values
            self: "modified_class" = original_class.__new__(cls, *args, **kwargs)

            # Type-check and replace
            for key, value_type in fields:
                # Make sure the attribute is an instance of the value type
                if not isinstance(getattr(self, key), value_type):
                    raise TypeError(f"Attribute {key!r} is not an instance of {value_type!r}")

            # Return the new tuple
            return self

    # Replace the name with the original name
    modified_class.__name__ = name

    # Return the modified class
    return modified_class


# Create lower-case name for ease-of-use
typedtuple = TypedTuple
