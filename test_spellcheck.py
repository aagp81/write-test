''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''
### WRITE IMPORT STATEMENTS HERE

import pytest
from spellcheck import word_count, char_count, first_char, last_char

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
#beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    assert word_count(input_value) < 10, f"Expected fewer than 10 words, but got {word_count(input_value)} words"

    assert char_count(input_value) < 50, f"Expected fewer than 50 characters, but got {word_count(input_value)} characters"

    return None

    raise NotImplementedError()

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string end with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    assert first_char(input_value).isupper(), "Expected the string to begin with a capital letter"

    assert last_char(input_value) == '.', "Expected the string to end with a period"

    return None

    raise NotImplementedError()

# Run these tests with `python3 -m pytest test_spellcheck.py`