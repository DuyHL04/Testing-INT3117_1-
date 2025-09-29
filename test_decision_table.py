import pytest
from ticket import ticket_cost  


test_cases = [
    (8, "Weekday", 50000),   # Rule 1
    (12, "Weekend", 60000),  # Rule 2
    (10, "abc", "Lỗi DayType"),  # Rule 3
    (20, "Weekday", 100000),  # Rule 4
    (30, "Weekend", 120000),  # Rule 5
    (40, "summer", "Lỗi DayType"),  # Rule 6
    (70, "Weekday", 70000), #Rule 7
    (80, "Weekend", 80000), #Rule 8
    (90, "time", "Lỗi DayType"), #Rule 9
    (-1, "Weekday", "Lỗi Age"), #Rule 10
    (150, "Weekend", "Lỗi Age"), #Rule 11
    (-5, "age", "Lỗi Age"), #Rule 12
]

@pytest.mark.parametrize("age,daytype,expected", test_cases)
def test_decision_table(age, daytype, expected):
    assert ticket_cost(age, daytype) == expected
