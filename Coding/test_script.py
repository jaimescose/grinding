import importlib
import pytest
problem = importlib.import_module('217_contains_duplicate')

@pytest.mark.parametrize("test,expected", problem.TEST_CASES)
def test_resukts(test, expected):
    print(test, expected)
