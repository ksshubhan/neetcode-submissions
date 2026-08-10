class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating hash map where we map each course to prerequisite list
        preMap = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[b].append(a)
        
        visit = set()

        def dfs(b):
            # base case
            if b in visit:
                return False
            
            if preMap[b] == []:
                return True
            
            visit.add(b)
            for pre in preMap[b]:
                if not dfs(pre): return False
            
            visit.remove(b)
            preMap[b] = []
            return True 

        for crs in range(numCourses):
            if not dfs(crs): return False 
        return True