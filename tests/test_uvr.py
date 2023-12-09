import pytest
from uvr import UVR


def test_method1():
    uvr = UVR()
    result = uvr.method1()
    assert result == expected_result, "Expected result does not match the actual result"

def test_method2():
    uvr = UVR()
    result = uvr.method2()
    assert result == expected_result, "Expected result does not match the actual result"

# ... repeat for each method in the UVR class ...
