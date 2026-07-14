import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = 0
        numbers = []
        operations = ["+", "*", "-", "/"]
        operation = ""

        while len(tokens) != 0:
            value = tokens.pop(0)
            if value not in operations:
                numbers.append(value)
            else:
                operation = value
                if operation == "+":
                    answer = int(numbers[-2]) + int(numbers[-1])
                    numbers[-1] = str(answer)
                    numbers.pop(-2)
                elif operation == "-":
                    answer = int(numbers[-2]) - int(numbers[-1])
                    numbers[-1] = str(answer)
                    numbers.pop(-2)
                elif operation == "*":
                    answer = int(numbers[-2]) * int(numbers[-1])
                    numbers[-1] = str(answer)
                    numbers.pop(-2)
                elif operation == "/":
                    answer = math.trunc(int(numbers[-2]) / int(numbers[-1]))
                    numbers[-1] = str(answer)
                    numbers.pop(-2)
        
        return int(numbers[0])
            