from add import add_me
import pytest

def test_add_me():
    
    assert add_me(1,3) == 4
    assert add_me(1.5,2.5) == pytest.approx(4.0)
    
pytest.main()
    