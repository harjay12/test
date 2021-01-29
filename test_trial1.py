import pytest
# import the function from your file
from trial1 import add_func


# Check if properly adds positive numbers
def test_add_positive():
    assert add_func(1,2) == 3

# Check if properly adds zero
def test_add_zero():
    assert add_func(1,0) == 1

# Check with negative number
def test_add_negative():
    assert add_func(4, -100) == -96

# Now check if it correctly produces error when provided so
def test_add_string_expect_exception():
    with pytest.raises(TypeError):
        add_func(4, 'I do not belong here')
