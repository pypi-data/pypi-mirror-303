from mypackage_tanyapeshkova import iterators

import pytest

def test_main():
    result = iterators.main()
    assert result == expected_value

if __name__ == '__main__':
    pytest.main()