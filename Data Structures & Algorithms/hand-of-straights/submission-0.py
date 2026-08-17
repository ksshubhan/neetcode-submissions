class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # initialise hash map 
        hash_map = {}

        # sort array 
        hand.sort()

        # populate hash map
        for i in range(len(hand)):
            if hand[i] not in hash_map:
                hash_map[hand[i]] = 1
            else:
                hash_map[hand[i]] += 1
        
        for i in range(len(hand)):
            if hash_map[hand[i]] == 0:
                continue
            else:
                for j in range(0, groupSize):
                    needed_card = hand[i] + j
                    if needed_card in hash_map and hash_map.get(needed_card) > 0:
                        hash_map[needed_card] -= 1
                    else:
                        return False
        
        return True 
            