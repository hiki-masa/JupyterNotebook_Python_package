from src import operations

def test_add():
    result = operations.add(1, 2)
    assert result == 3 # Trueとなる条件
    
def test_subtract():
    result = operations.subtract(3, 1)
    assert result == 2
    
def test_multi():
    result = operations.multi(2, 3)
    assert result == 6
    
def test_division():
    q, r = operations.division(7, 3)
    assert q == 2
    assert r == 1