class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        routes = []
        start = "JFK"
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            routes.append(a)

        dfs("JFK")

        return routes[::-1]

