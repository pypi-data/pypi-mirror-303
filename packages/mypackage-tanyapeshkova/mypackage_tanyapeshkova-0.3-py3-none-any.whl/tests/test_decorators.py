import pytest
from mypackage_tanyapeshkova import decorators

def test_main():
    result = decorators.main()
    assert result == expected_value

if __name__ == '__main__':
    pytest.main()