class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        maxp=0
        for i in prices:
            if i<min:
                min=i
            profit=i-min
            if profit>maxp:
                maxp=profit
        return maxp
        