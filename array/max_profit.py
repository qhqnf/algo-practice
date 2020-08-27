from typing import List
import sys

testcase = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_price = sys.maxsize

        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(prices[i] - min_price, profit)

        return profit


if __name__ == "__main__":
    solution = Solution().maxProfit(testcase)
    print(solution)
