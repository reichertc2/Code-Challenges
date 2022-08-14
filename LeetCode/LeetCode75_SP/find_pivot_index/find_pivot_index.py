class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_reversed = nums[::-1]
        count_l = 0
        count_r = 0
        # print(nums_reversed)
        for idx, number in enumerate(nums):
            count_r += nums_reversed[idx]
            if count_l == count_r and count_l != 0:
                print(idx)
                return idx
            count_l += number

            # print(idx)
            print("count_l ", count_l)
            print("count_r ", count_r)
            # print(nums_reversed[idx])

        return -1


nums = [1, 7, 3, 6, 5, 6]
sol = Solution()
print(sol.pivotIndex(nums))
