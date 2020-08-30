from typing import List

testcase = [73, 74, 75, 71, 69, 72, 76, 73]


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        answer = [0] * len(T)
        stack = []

        for i, v in enumerate(T):

            # pop value in stack and append to answer list
            while stack and v > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last

            stack.append(i)

        return answer


if __name__ == "__main__":
    solution = Solution().dailyTemperatures(testcase)
    print(solution)
