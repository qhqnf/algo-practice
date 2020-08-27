from typing import List

testcase = [1, 4, 3, 2]


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        """
        # delcare variable
        sum = 0
        pair = []
        
        # sort list
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair)==2:
                sum += min(pair)
                pair = []
        """

        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    solution = Solution().arrayPairSum(testcase)
    print(solution)
