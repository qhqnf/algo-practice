testcase = "{}()[]"


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char not in dict:
                stack.append(char)
            elif dict[char] != stack.pop():
                return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution().isValid(testcase)
    print(solution)
