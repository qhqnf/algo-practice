from typing import List

testcase = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


if __name__ == "__main__":
    solution = Solution().trap(testcase)
    print(solution)
