class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(0, n+1)]

        rank = [1]*(n+1)

        def find(node):
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

        for n1, n2 in edges:
            if find(n1) == find(n2):
                return [n1, n2]
            else:
                union(n1, n2)
