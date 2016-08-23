class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        revProduct = nums[:]
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                revProduct[i] = 1
            else:
                revProduct[i] = nums[i+1] * revProduct[i+1]
        leftProductResult = 1
        for i in range(0, len(nums)):
            revProduct[i] *= leftProductResult
            leftProductResult *= nums[i]
        return revProduct