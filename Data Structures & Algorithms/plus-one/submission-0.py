class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        number += 1
        res = list(map(int, str(number)))
        return res