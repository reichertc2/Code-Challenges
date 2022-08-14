import pytest
from LeetCode.RandomProblems.zigzag_conversion.zigzag_conversion import Solution


# @pytest.mark.skip(reason="not finished")
def test_leetcode_1():
    sol = Solution()
    actual = sol.convert("A", 1)
    expected = "A"
    assert actual == expected

@pytest.mark.skip(reason="not finished")
def test_leetcode_1_a():
    sol = Solution()
    actual = sol.convert("ABCD", 2)
    expected = "ADBC"
    assert actual == expected


@pytest.mark.skip(reason="not finished")
def test_leetcode_2():
    sol = Solution()
    actual = sol.convert("PAYPALISHIRING", 4)
    expected = "PAHNAPLSIIGYIR"
    assert actual == expected


@pytest.mark.skip(reason="not finished")
def test_leetcode_3():
    sol = Solution()
    actual = sol.convert("PAYPALISHIRING", 3)
    expected = "PINALSIGYAHRPI"
    assert actual == expected
