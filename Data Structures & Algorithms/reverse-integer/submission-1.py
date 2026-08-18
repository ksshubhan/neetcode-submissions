class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX =  (2**31) - 1
        MIN = -2**31
        negative = False

        if x < 0:
            x = x * -1
            negative = True

        while x != 0:
            right_most = x % 10
            if res > MAX / 10 or res < MIN / 10:
                return 0
            elif res == MAX / 10 and right_most > MAX % 10:
                return 0
            elif res == MIN / 10 and right_most < MIN % 10:
                return 0
            else:
                res = res * 10
                res = res + right_most
                x = x // 10
        
        return -1 * res if negative else res 