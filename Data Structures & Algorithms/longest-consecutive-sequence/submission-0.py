class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        length=0
        for i in nums:
            lenn=1
            if i-1 not in num:
                while i+1 in num:
                    lenn+=1
                    i+=1
            length=max(lenn,length)
        return length