class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        min_price, max_profit = prices[0], 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


def test_solution():
    prices = [7,1,5,3,6,4]
    assert Solution().maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert Solution().maxProfit(prices) == 0
