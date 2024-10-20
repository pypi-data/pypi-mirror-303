from runtypes import *


def test_optional_parameters():

    def _validate(value, *optionals):
        assert not optionals

    my_type = RunType("MyType", checker=_validate)

    assert isinstance("Test", my_type)
    assert not isinstance("Test", my_type["Test"])
