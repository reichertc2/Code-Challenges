from LeetCode.LeetCode75_SP.running_sum_of_array.running_sum_of_array import Solution
import pytest


def test_leetcode_1():
    sol = Solution()
    nums = [1, 2, 3, 4]
    actual = sol.runningSum(nums)
    expected = [1, 3, 6, 10]
    assert actual == expected


def test_leetcode_2():
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    actual = sol.runningSum(nums)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_leetcode_3():
    sol = Solution()
    nums = [3, 1, 2, 10, 1]
    actual = sol.runningSum(nums)
    expected = [3, 4, 6, 16, 17]
    assert actual == expected
