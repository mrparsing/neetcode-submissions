class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)

        for t in trust:
            adj[t[0]].append(t[1])

        nodes = set(adj.keys())
        judge = -1
        for i in range(1, n+1):
            if i not in nodes:
                judge = i
                break
        for k, v in adj.items():
            if judge not in v:
                judge = -1
                break
        return judge