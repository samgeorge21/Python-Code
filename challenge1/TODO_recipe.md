1. The Problem: 
As a user, so that I can keep track of my tasks, I want to check if a text includes 'TODO'.

2. The Structure:
Name - def check_for_todo(text):
Parameters - initially none, text as a string.
Return value - if True, returns text to confirm string includes TODO. If False, returns message to say string does not include 'TODO'.
Side effects - none expected

3. Tests:
T1 - check the function can be called
def test_check_can_be_called():
    assert check_for_TODO() == True

T2 - check the function can accept and return a string
def test_returns_string():
    assert check_for_TODO("text") == 'text'

T3 - check a function can detect 'TODO' within a string
def test_detects_TODO():
    assert check_for_TODO("contains TODO") == True

T4 - check a function can detect 'TODO' not within a string
def test_detects_no_TODO():
    assert check_for_TODO("contains something else") == False

T5 - check function returns confirmation message if string contains 'TODO'
def test_return_confirmation_message():
    assert check_for_TODO("contains TODO") == 'The text includes TODO'

T6 - check function returns message to state 'TODO' not in string
def test_TODO_not_in_string():
    assert check_for_TODO("contains something else") == 'The text does not include TODO'

T7 - check function only accepts a string and gives message if anything other than a string is provided as the argument
def test_not_a_string():
    assert check_for_TODO(57) == 'This function will only accept a string of text'


4. Implementation:
Follow the red, green, refactor process to implement the desired behaviour