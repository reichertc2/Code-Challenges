import pytest
from CodeWars.vowel_count.vowel_count import get_count

def test_code_wars_1():
    expected = 5
    actual = get_count('aeiou')
    assert actual == expected