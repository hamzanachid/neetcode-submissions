class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        maxOut=0
        while i<len(prices)-1:
           maxx=max(prices[i+1:])
           maxOut=max(maxOut,maxx-prices[i])
           i+=1
        return maxOut   