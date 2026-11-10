class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)

        return result