#给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#示例 1:
#
#    输入: [3,3,5,0,0,3,1,4]
#    输出: 6
#    解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#         随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#示例 2:
#
#    输入: [1,2,3,4,5]
#    输出: 4
#    解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#示例 3:
#
#    输入: [7,6,4,3,1]
#    输出: 0
#    解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。



#思路:
#    此题交易次数是最多2次,有点困难.
#
#    同一天我们要考虑四种情况.
#
#    buy1[i] = max(buy1[i-1], -prices[i])
#
#    sell1[i] = max(sell1[i-1],buy1[i-1] + prices[i] )
#
#    buy2[i] = max(buy2[i-1], sell1[i-1] - prices[i])
#
#    sell2[i] = max(sell2[i-1], buy2[i-1] + prices[i])
#
#    其实就是2次交易次数为1的相加(参考第一题).
#
#    特别注意第三个等式,就是在第一次卖过之后在买入.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        buy1 = [0] * n
        sell1 = [0] * n
        buy2 = [0] * n
        sell2 = [0] * n
        buy1[0] = -prices[0]
        buy2[0] = -prices[0]
        for i in range(1, n):
            buy1[i] = max(buy1[i-1], -prices[i])
            sell1[i] = max(sell1[i-1], buy1[i-1] + prices[i])
            buy2[i] = max(buy2[i-1], sell1[i-1]-prices[i])
            sell2[i] = max(sell2[i-1], buy2[i-1]+prices[i])
        return sell2[-1]