import pytest

parameters = [1, 2, 3, 4]


@pytest.mark.parametrize('digit', parameters)
def test_one(digit):
    print(digit)
    pass