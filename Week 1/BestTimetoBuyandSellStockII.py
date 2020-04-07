"""
Task 5:
    Say you have an array for which the ith element is the price of a given 
    stock on day i.
    Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (i.e., buy one and sell 
    one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time 
    (i.e., you must sell the stock before you buy again).
"""
# 60 ms
class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
     def maxProfit(prices):
        p = prices[0]
        profit = 0
        if len(prices) == 0: return 0
        for price in prices[1:]:
            if price - p > 0:
                profit += (price - p)
                p = price
            else: 
                p = price    
        return profit        

#Tests     
array = [7,1,5,3,6,4]
print(Solution.maxProfit(array))  
array = [1,2,3,4,5]
print(Solution.maxProfit(array)) 
array = [7,6,4,3,1]
print(Solution.maxProfit(array)) 
