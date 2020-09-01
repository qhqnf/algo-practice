class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        counter = collections.Counter(nums).most_common(k)
        answer = []
        
        for i in range(k):
            answer.append(counter[i][0])
            
        return answer
        """

        return list(zip(*collections.Counter(nums).most_common(k)))[0]
