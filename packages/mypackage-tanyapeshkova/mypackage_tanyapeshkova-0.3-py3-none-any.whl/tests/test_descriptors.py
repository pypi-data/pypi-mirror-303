
import pytest
from mypackage_tanyapeshkova import descriptors

def test_main():
    result = descriptors.main()
    assert result == expected_value

if __name__ == '__main__':
    pytest.main()