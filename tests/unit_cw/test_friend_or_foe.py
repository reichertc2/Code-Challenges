import pytest
from CodeWars.friend_or_foe.friend_or_foe import friend


def test_codewars_1():
    expected = ["Ryan", "Mark"]
    actual = friend(["Ryan", "Kieran", "Mark",])
    assert actual == expected