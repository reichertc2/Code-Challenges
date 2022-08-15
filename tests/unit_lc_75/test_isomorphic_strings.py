from LeetCode.LeetCode75_SP.isomorphic_strings.isomorphic_strings import Solution
import pytest


# @pytest.mark.skip(reason="not ready yet")
def test_leetcode_1():
    sol = Solution()
    s = 'egg'
    t = 'add'
    actual = sol.isIsomorphic(s, t)
    expected = True
    assert actual == expected


# @pytest.mark.skip(reason="not ready yet")
def test_leetcode_2():
    sol = Solution()
    s = 'foo'
    t = 'bar'
    actual = sol.isIsomorphic(s, t)
    expected = False
    assert actual == expected


# @pytest.mark.skip(reason="not ready yet")
def test_leetcode_3():
    sol = Solution()
    s = 'paper'
    t = 'title'
    actual = sol.isIsomorphic(s, t)
    expected = True
    assert actual == expected
