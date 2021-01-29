import pytest

from trial1 import func

def test_str():
    t="Hello World!"
    assert func(t)


def test_exception():
    with pytest.raises(TypeError):
        func(5,'')