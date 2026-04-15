class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res=[]
        for sub in self.permuteUnique(nums[1:]):
            for i in range(len(sub)+1):
                s=sub.copy()
                s.insert(i,nums[0])
                if s not in res:
                    res.append(s)
        return res
