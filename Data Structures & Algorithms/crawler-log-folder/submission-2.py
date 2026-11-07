class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minimum = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                minimum = max(0, minimum-1)
            else:
                minimum += 1
        return minimum