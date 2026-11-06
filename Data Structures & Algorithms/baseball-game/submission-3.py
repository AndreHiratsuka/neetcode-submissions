class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            if operation == "+":
                # Sum the two previous valid scores.
                scores.append(scores[-1] + scores[-2])

            elif operation == "D":
                # Double the previous valid score.
                scores.append(scores[-1] * 2)

            elif operation == "C":
                # Remove the previous valid score.
                scores.pop()

            else:
                # Convert the score to int only once.
                scores.append(int(operation))

        return sum(scores)