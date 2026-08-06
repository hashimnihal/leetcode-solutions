class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        occurense=1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                occurense+=1
            else:
                occurense=1
            if occurense<=2:
                nums[index]=nums[i]
                index+=1
        return index
