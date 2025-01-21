# app.py
# Python script to reverse a string and check if it is a palindrome.

def reverse_string(s):
    "
    return s[::-1]

def is_palindrome(s):
    
    reversed_s = reverse_string(s)
    return s == reversed_s

# Unit tests for the functions
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True  

