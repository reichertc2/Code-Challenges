from LeetCode.LeetCode75_SP.find_pivot_index.find_pivot_index import Solution
import pytest

@pytest.mark.skip(reason="not ready")
def test_leetcode_1():
    sol = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    actual = sol.pivotIndex(nums)
    expected = 3
    assert actual == expected


@pytest.mark.skip(reason="not ready")
def test_leetcode_2():
    sol = Solution()
    nums = [1, 2, 3]
    actual = sol.pivotIndex(nums)
    expected = -1
    assert actual == expected


@pytest.mark.skip(reason="not ready")
def test_leetcode_3():
    sol = Solution()
    nums = [2, 1, -1]
    actual = sol.pivotIndex(nums)
    expected = 0
    assert actual == expected
