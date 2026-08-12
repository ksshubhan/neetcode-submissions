class Solution:
    # We can solve this leetcode by using union by find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we create an array to keep track of the parents of each node
        # initially we assume each node is its own parent
        parent = [i for i in range(n)]

        # we create another array to keep track of the size of components
        # as we connected edges the size of components will increase
        # but initially because each node is its own parent and there are n nodes
        # we have a n components of size 1 to start off with
        rank = [1]*n
        
        # find function
        # the purpose of this function is to find the root of the component
        # that node belongs to 
        # and a component is a group of nodes that are connected together
        def find(node):
            # initially we set res to the current node
            res = node

            # while we have not reached root 
            # make current node skip one level upward
            # move to that higher node
            while res != parent[res]:
                # path compression because we move node closer to root
                # it makes future find() operations faster
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            # the loop stops when find the root at which point we return it
            return res
        
        # 
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            # if they are already connected no merging is needed 
            # so we return 0 because no new nodes are added 
            # number of nodes stay the same 
            if p1 == p2:
                return 0
            
            # if we reach here then p1 and p2 belong to different components
            
            # we attach the smaller sizes component to the larger one
            # if and else depending on which one p1 or p2 is bigger than the other 
            if rank[p2] > rank[p1]:
                # merge
                parent[p1] = p2
                # update size of components
                rank[p2] += rank[p1]
            
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            # because we merged then component count will increase by 1 
            return 1 

        # initially we assume very node is seperate 
        res = n
        # for each edge in edges
        for n1, n2 in edges:
            # if union successfully merges nodes
            # then res decreases by 1 because we have 1 less components
            # e.g. if we 5 indiviausl nodes and edge joins 2 of them now we have
            # 4 components in total etc.. 
            res -= union(n1, n2)
        
        # we return the final result 
        return res