from typing import List

testcase = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero",
]


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter = []
        digit = []

        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter + digit


if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderLogFiles(logs=testcase))
