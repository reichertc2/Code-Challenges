class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        last_idx = 0
        for number in nums:
            last_idx += number
            new_list.append(last_idx)

        return new_list



