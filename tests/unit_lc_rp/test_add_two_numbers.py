import pytest
from LeetCode.RandomProblems.add_two_numbers.add_two_numbers import Solution, ListNode

@pytest.mark.skip(reason="not finished")
def test_leetcode_1():
    sol = Solution()
    sol.addTwoNumbers()

@pytest.mark.skip(reason="not finished")
def test_build_node_list():
    num_list = [1,5,3,5]
    sol = Solution()
    actual = sol.build_node_list(num_list)
    expected = ''
    assert actual == expected

