from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                # Store numbers as integers immediately.
                stack.append(int(token))
                continue

            # Order matters:
            # In "a b operator", b is popped first.
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            else:
                # int() truncates toward zero.
                result = int(a / b)

            stack.append(result)

        return stack[-1]