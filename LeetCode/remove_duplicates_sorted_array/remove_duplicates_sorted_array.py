class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


    

        nums[:] = set(nums)
        nums.sort()
        # new_list = list(new_set)
        # list_len = len(new_list)
        return len(nums)   