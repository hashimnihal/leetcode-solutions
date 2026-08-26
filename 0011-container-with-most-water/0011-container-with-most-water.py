class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while(l<r):
            w=r-l
            ht=min(height[l],height[r])
            y=w*ht
            ans=max(ans,y)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans