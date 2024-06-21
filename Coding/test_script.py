import importlib

import pytest
problem = importlib.import_module('coding.217_contains_duplicate')

@pytest.mark.parametrize("test,expected", problem.TEST_CASES)
def test_results(test, expected):
    result = problem.main(test)
    assert result == expected
