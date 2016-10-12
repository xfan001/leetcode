class Solution:
    def subsets(self, nums):
        results = [[]]
        self.helper(nums, results, 0)
        return results

    def helper(self, nums, S, index):
        if index==len(nums):
            return
        isRepeat = False
        if not isRepeat:
            extraS = []
            for lst in S:
                new_lst = lst[:]
                new_lst.append(nums[index])
                extraS.append(new_lst)
            S += extraS
        self.helper(nums, S, index+1)