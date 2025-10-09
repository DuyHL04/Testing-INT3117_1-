import pytest
from ticket import ticket_cost  

#Test Child
@pytest.mark.parametrize("age", [0, 1, 6, 11, 12])
@pytest.mark.parametrize("daytype,expected", [
    ("Weekday", 50000),
    ("Weekend", 60000),
])
def test_child_bva(age, daytype, expected):
    assert ticket_cost(age, daytype) == expected

#Test Adult
@pytest.mark.parametrize("age", [13, 14, 24, 59, 60])
@pytest.mark.parametrize("daytype,expected", [
    ("Weekday", 100000),
    ("Weekend", 120000),
])
def test_adult_bva(age, daytype, expected):
    assert ticket_cost(age, daytype) == expected

#Test Senior
@pytest.mark.parametrize("age", [61, 62, 81, 99, 100])
@pytest.mark.parametrize("daytype,expected", [
    ("Weekday", 70000),
    ("Weekend", 80000),
])
def test_senior_bva(age, daytype, expected):
    assert ticket_cost(age, daytype) == expected
