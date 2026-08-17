class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if amount of gas needed to complete entire circuit is less 
        # than cost then return -1 
        if sum(gas) < sum(cost):
            return -1
        
        # initialise total
        total = 0

        # initialise res_index
        # this is our current candidate starting station
        res_index = 0

        # iterate through gas stations from res_index to end of list 
        for i in range(res_index, len(gas)):
            # after filling up at gas station i and paying to travel to next
            # station what is my net gain or loss 
            difference = gas[i] - cost[i]
            
            #  we add this net gain or loss to total
            # total represents how much fuel you currently have since starting from
            # res_index. 
            total += difference

            # if we reach here it means starting from station at res index
            # we could not make it past station i so that starting position failed
            if total < 0:
                # re-initialise total to 0
                total = 0
                
                # the next possible starting station is the station immediately 
                # after where we failed
                res_index = i + 1   
        
        # return station at res_index
        # this is the station we need to start from to allow to us traverse
        # every station
        return res_index