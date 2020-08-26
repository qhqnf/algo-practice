from typing import List
import collections

testcase = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return anagrams.values()


if __name__ == "__main__":
    solution = Solution().groupAnagrams(testcase)
    print(solution)
