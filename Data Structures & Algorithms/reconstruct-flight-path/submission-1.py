class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []

        def visit(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                visit(next_airport)

            result.append(airport)

        visit("JFK")
        return result[::-1]

        
        