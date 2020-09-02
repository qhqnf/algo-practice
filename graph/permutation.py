class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        answer = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                answer.append(prev_elements[:])
                
            for i in elements:
                next_elements = elements[:]
                prev_elements.append(i)
                next_elements.remove(i)
                
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        
        return answer
        """

        return list(map(list, itertools.permutations(nums)))

