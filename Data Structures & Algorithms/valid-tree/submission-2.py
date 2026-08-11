class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()

        preMap = {i:[] for i in range(n)}

        for pre_node, node in edges:
            preMap[node].append(pre_node)
            preMap[pre_node].append(node)

        def dfs(node, parent):

            if node in visit:
                return False
            
            visit.add(node)

            for pre in preMap[node]:
                if pre == parent:
                    continue
                if not dfs(pre, node):
                    return False

            return True


        if not dfs(0, -1):
            return False

        return len(visit) == n