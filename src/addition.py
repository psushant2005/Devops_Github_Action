# app.py
# This is a test commit
def add(a, b):
    return a + b
# commit for testing
def sub(x, z):
    return z - x

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
# commit for testing
def test_sub():
    assert sub(2, 3) == 1
    assert sub(-3, 3) == 6
