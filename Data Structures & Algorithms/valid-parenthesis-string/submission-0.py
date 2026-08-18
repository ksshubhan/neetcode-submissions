class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_1 = []
        stack_2 = []

        for i in range(len(s)):
            if s[i] == "(":
                stack_1.append(i)
            elif s[i] == "*":
                stack_2.append(i)
            elif s[i] == ")":
                if len(stack_1) > 0:
                    stack_1.pop(-1)
                elif len(stack_2) > 0:
                    stack_2.pop(-1)
                else:
                    return False 
        
        while len(stack_1) > 0 and len(stack_2) > 0:
            if stack_2[-1] >= stack_1[-1]:
                stack_1.pop(-1)
                stack_2.pop(-1)
            else:
                return False
        
        if len(stack_1) > 0:
            return False
        else:
            return True 
        
