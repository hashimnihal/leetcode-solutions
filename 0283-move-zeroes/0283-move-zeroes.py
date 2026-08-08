class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[n]
                nums[n]=nums[i]
                nums[i]=temp
                n+=1
            
        return n
