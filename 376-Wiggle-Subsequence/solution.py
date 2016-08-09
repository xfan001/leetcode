class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        diff = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        length = 0 if diff[0]==0 else 1
        expect_p = diff[0]<0
        for i in range(1, len(diff)):
            if expect_p and diff[i]<=0:
                continue
            if (not expect_p) and diff[i]>=0:
                continue
            expect_p = diff[i]<0
            length += 1
        return length+1