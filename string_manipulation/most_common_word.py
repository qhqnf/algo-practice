from typing import List
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = []
        temp = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split()]
        for word in temp:
            if word not in banned:
                words.append(word)

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.mostCommonWord(paragraph, banned))
