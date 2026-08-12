from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        visit = set()
        visit.add(beginWord)

        hash_map = defaultdict(list)

        queue = [beginWord]

        for word in wordList:
            for i in range(len(word)):
                original = word
                word = list(word)
                word[i] = "*"
                hash_map["".join(word)].append(original)
                word = original

    
        def bfs(ladder):
            if endWord not in wordList:
                return 0
            

            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    w = queue.pop(0)
                    w_l = list(w)
                    for i in range(len(w_l)):
                        w_l = list(w)
                        w_l[i] = "*"
                        pattern = hash_map["".join(w_l)]
                        if pattern:
                            for p in pattern:
                                if p not in visit:
                                    queue.append(p)
                                    visit.add(p)
                                if p == endWord:
                                    return ladder + 1
                ladder += 1
            
            return 0
            
        res = bfs(1)
        return res



                

        