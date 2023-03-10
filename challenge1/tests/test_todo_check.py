import pytest
from lib.todo_check import *

""""
T1 - check the function can be called
"""

#def test_check_can_be_called():
#    assert check_for_TODO() == True

"""
T2 - check the function can accept and return a string
"""

#def test_returns_string():
#    assert check_for_TODO("text") == 'text'

"""
T3 - check a function can detect 'TODO' within a string
"""

#def test_detects_TODO():
#    assert check_for_TODO("contains TODO") == True

"""
T4 - check a function can detect 'TODO' not within a string
"""

#def test_detects_no_TODO():
#    assert check_for_TODO("contains something else") == False

"""
T5 - check function returns confirmation message if string contains 'TODO'
'"""

def test_return_confirmation_message():
    assert check_for_TODO("contains TODO") == 'The text includes TODO'

"""
T6 - check function returns message to state 'TODO' not in string
"""

def test_TODO_not_in_string():
    assert check_for_TODO("contains something else") == 'The text does not include TODO'

"""
T7 - check function only accepts a string and gives message if anything other than a string is provided as the argument
THIS HAS BEEN TESTED WITH INTEGER, FLOAT AND BOOLEAN - ALL PASSED
"""

def test_not_a_string():
    assert check_for_TODO(0.4546463) == 'This function will only accept a string of text'