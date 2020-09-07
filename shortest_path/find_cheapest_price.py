class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        graph = collections.defaultdict(list)

        for x, y, z in flights:
            graph[x].append((y, z))

        k = 0
        Q = [(0, src, k)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price

            if k <= K:
                k += 1
                for y, z in graph[node]:
                    alt = price + z
                    heapq.heappush(Q, (alt, y, k))

        return -1
