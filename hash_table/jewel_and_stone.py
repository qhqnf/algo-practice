class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        freqs = collections.defaultdict(int)
        sum = 0
        
        for char in S:
            freqs[char] += 1
            
        for char in J:
            if char in freqs:
                sum += freqs[char]
        
        return sum
        
        
        '''
        return sum([s in J for s in S])
        '''