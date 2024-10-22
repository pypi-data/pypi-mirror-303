
from mypackage_tanyapeshkova import generators
import pytest

def test_main():
    result = generators.main()
    assert result == expected_value

if __name__ == '__main__':
    pytest.main()