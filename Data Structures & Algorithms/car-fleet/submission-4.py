class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        stack = []
        for i, p in enumerate(position):
            res.append([p, i])
        sorted_res = sorted(res, key=lambda x: x[0], reverse=True)

        for i in sorted_res:
            time = (target - i[0]) / speed[i[1]]
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)