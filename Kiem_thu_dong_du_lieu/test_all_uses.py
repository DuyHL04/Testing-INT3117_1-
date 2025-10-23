# test_paths_C2.py
import pytest
from ticket import ticket_cost

# --- Error cases ---
def test1():
    assert ticket_cost(-5, "Weekday") == "Invalid Age"

def test2():
    assert ticket_cost(5, "hello") == "Invalid Daytype"

# --- Normal price cases (Child) ---
def test3():
    assert ticket_cost(5, "Weekday") == 50000

def test4():
    assert ticket_cost(30, "Weekday") == 100000

# --- Normal price cases (Adult) ---
def test5():
    assert ticket_cost(80, "Weekday") == 70000

def test6():
    assert ticket_cost(5, "Weekend") == 60000

# --- Normal price cases (Senior) ---
def test7():
    assert ticket_cost(30, "Weekend") == 120000

def test8():
    assert ticket_cost(80, "Weekend") == 80000
