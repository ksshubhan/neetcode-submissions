class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        visit = set()

        path = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
             
            
            visit.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)

            preMap[crs] = []

            if crs not in path:
                path.append(crs)

            return True
            
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return path
        