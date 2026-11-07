class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minimum = []
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if len(minimum) != 0:
                    minimum.pop()
            else:
                minimum.append(log)
        return len(minimum)