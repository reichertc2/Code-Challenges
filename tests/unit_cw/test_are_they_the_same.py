import pytest
from CodeWars.are_they_the_same.are_they_the_same import comp

def test_code_wars_1():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    expected = True
    actual = comp(a1,a2)
    assert actual == expected


def test_code_wars_2():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    expected = False
    actual = comp(a1,a2)
    assert actual == expected

def test_code_wars_3():
    a1 = []
    a2 = []
    expected = True
    actual = comp(a1,a2)
    assert actual == expected