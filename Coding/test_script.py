import importlib

import pytest
problem = importlib.import_module('coding.242_valid_anagram')

@pytest.mark.parametrize("test,expected", problem.TEST_CASES)
def test_results(test, expected):
    print(test, expected)
    result = problem.main(*test)
    assert result == expected
