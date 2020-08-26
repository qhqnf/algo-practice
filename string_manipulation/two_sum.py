from typing import List

nums = [2, 7, 11, 15]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for i, value in enumerate(nums):
            nums_map[value] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]


if __name__ == "__main__":
    solution = Solution().twoSum(nums, target)
    print(solution)
