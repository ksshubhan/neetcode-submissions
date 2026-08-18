class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c, = target
        
        found_a = False
        found_b = False
        found_c = False
        
        for i in range(len(triplets)):
            if triplets[i][0] > a or triplets[i][1] > b or triplets[i][2] > c:
                continue
            if triplets[i][0] == a:
                found_a = True
            if triplets[i][1] == b:
                found_b = True
            if triplets[i][2] == c:
                found_c = True 
            
        return found_a and found_b and found_c