from src import operations

def test_add():
    result = operations.add(1.5, 2.4)
    assert result == 3.9
    
def test_subtract():
    result = operations.subtract(1.25, 0.125)
    assert result == 1.125
    
def test_multi():
    result = operations.multi(1.25, 2.75)
    assert result == 3.4375