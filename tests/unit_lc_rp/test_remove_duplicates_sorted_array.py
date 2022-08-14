from LeetCode.RandomProblems.remove_duplicates_sorted_array.remove_duplicates_sorted_array import Solution
import pytest


def test_leetcode_1():
    sol = Solution()
    nums = [1, 1, 2]
    actual = sol.removeDuplicates(nums)
    expected = 2
    assert actual == expected


@pytest.mark.skip(reason="not working properly")
def test_leetcode_2():
    sol = Solution()
    nums = [1, 1, 2]
    actual = sol.removeDuplicates(nums)
    expected = 2
    expected_nums = [1, 2]
    for number in expected_nums:
        assert nums[number] == expected_nums[number]
