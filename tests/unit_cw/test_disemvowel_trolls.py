import pytest
from CodeWars.disemvowel_trolls.disemvowel_trolls import disemvowel

def test_codewars_test_1():
    expected = "Ths wbst s fr lsrs LL!"
    actual = disemvowel("This website is for losers LOL!")
    assert expected == actual