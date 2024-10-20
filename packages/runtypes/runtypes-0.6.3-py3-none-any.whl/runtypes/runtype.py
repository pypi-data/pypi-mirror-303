import typing
import inspect


def _assert(_condition: bool, _error: str) -> None:
    # Check the value and raise accordingly
    if not _condition:
        raise TypeError(_error)


def _assert_istype(_value: typing.Any, _type: type) -> None:
    # Check the instance
    _assert(type(_value) == _type, f"Value is not of type {_type.__name__}")


def _assert_isinstance(_value: typing.Any, _type: typing.Any) -> None:
    # Check the instance
    _assert(isinstance(_value, _type), f"Value is not an instance of {_type}")


class ArgumentError(KeyError):
    pass


def _resolve_function_arguments(function: typing.Callable[..., typing.Any], args: typing.Sequence[typing.Any], kwargs: typing.Dict[str, typing.Any], strict: bool = False) -> typing.Dict[str, typing.Any]:
    # Get the function signature
    signature = inspect.signature(function)

    # Create a dictionary for arguments
    arguments = {}

    # Loop over variable names and fetch the respective variable
    for index, (name, parameter) in enumerate(signature.parameters.items()):
        # Check whether the argument is provided via args
        if index < len(args):
            arguments[name] = args[index]
            continue

        # Check whether the argument is provided via kwargs
        if name in kwargs:
            arguments[name] = kwargs[name]
            continue

        # Check whether the argument is provided via defaults
        if parameter.default is not inspect._empty:
            arguments[name] = parameter.default
            continue

        # Make sure argument is not a positional
        if parameter.kind == inspect._VAR_POSITIONAL:
            continue

        # Argument was not provided!
        if strict:
            raise ArgumentError(f"Argument {name!r} was not provided")

    # Return the arguments
    return arguments


class RunType(object):

    def __init__(self, name: str, caster: typing.Optional[typing.Callable[..., typing.Any]] = None, checker: typing.Optional[typing.Callable[..., None]] = None, arguments: typing.List[type] = []) -> None:
        # Make sure the name is a string
        _assert_istype(name, str)

        # Make sure at least one of caster or checker are defined
        _assert(any([caster, checker]), "At least one of caster or checker must be defined")

        # Make sure the caster is callable if defined
        if caster is not None:
            _assert(callable(caster), "Caster must be callable")

        # Make sure the checker is a callable if defined
        if checker is not None:
            _assert(callable(checker), "Checker must be callable")

        # Make sure arguments are a list or none
        if arguments:
            _assert_isinstance(arguments, list)

        # Decide the name
        self._name = name

        # Set internal checker and caster
        self._caster = caster
        self._checker = checker
        self._arguments = arguments

    def cast(self, value: typing.Any) -> typing.Any:
        # If the type caster is defined, execute it
        if self._caster:
            # Make sure all caster arguments have been resolved
            _resolve_function_arguments(self._caster, [value] + self._arguments, {}, strict=True)

            # Use the caster to cast the value
            return self._caster(value, *self._arguments)

        # Fallback - check using type checker, then return value
        self.check(value)

        # Return original value
        return value

    def check(self, value: typing.Any) -> None:
        # If the type checker is defined, execute it
        if self._checker:
            # Make sure all caster arguments have been resolved
            _resolve_function_arguments(self._checker, [value] + self._arguments, {}, strict=True)

            # Execute type checker with arguments
            self._checker(value, *self._arguments)

            # Nothing more to do
            return

        # Fallback - check using type caster
        _assert(value == self.cast(value), f"Casted value does not match input value")

    def __call__(self, value: typing.Any) -> typing.Any:
        # Try casting the value
        return self.cast(value)

    def __instancecheck__(self, value: typing.Any) -> bool:
        try:
            # Try type-checking
            self.check(value)

            # Type-checking passed
            return True
        except ArgumentError:
            # Re-raise
            raise
        except:
            # Type-checking failed
            return False

    def __getitem__(self, argument: typing.Any) -> "RunType":
        # Make sure object is not already subscripted
        if self._arguments:
            raise NotImplementedError(f"Cannot subscript an already subscripted type {self!r}")

        # Convert index into list
        if isinstance(argument, tuple):
            arguments = list(argument)
        else:
            arguments = [argument]

        # Return a subscripted validator
        return self.__class__(caster=self._caster, checker=self._checker, name=self._name, arguments=arguments)

    def __repr__(self) -> str:
        # Create initial representation
        representation = self._name

        # If there are any arguments, add them to the representation
        if self._arguments:
            representation += repr(self._arguments)

        # Return the generated representation
        return representation


# Decorator for easy typechecker creating
def typechecker(function: typing.Callable[..., typing.Any]) -> RunType:
    return RunType(function.__name__, function)
