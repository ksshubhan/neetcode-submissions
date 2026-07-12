class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        total = 0
        print(l)
        print(r)
        total = numbers[l] + numbers[r]
        while total != target:
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                break
            total = numbers[l] + numbers[r]

        return [l + 1, r + 1]