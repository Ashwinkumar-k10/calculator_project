def test_add():
    """Test add function."""
    assert add(2,3) == 5

def test_subtract():
    """Test subtract function."""
    assert subtract(5,2) == 3

def test_multiply():
    """Test multiply function."""
    assert multiply(2,3) == 6

def test_divide():
    """Test divide function."""
    assert divide(6,2) == 3

def test_divide_by_zero():
    """Test division by zero."""
    try:
        divide(5,0)
        assert False
    except ValueError:
        assert True
