class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        seen={}
        for i,num in enumerate(sorted_nums):
            if num not in seen:
                seen[num]=i
        ans=[]
        for num in nums:
            ans.append(seen[num])
        return ans 
            