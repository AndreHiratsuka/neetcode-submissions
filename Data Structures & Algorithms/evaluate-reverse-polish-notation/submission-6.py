class Solution:
    def is_number(seçf, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(token)
                print(token)
            elif token == "+":
                result = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(result)
                # print(result)
            elif token == "-":
                result = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
                # print(result)
            elif token == "*":
                result = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(result)
                # print(result)
            elif token == "/":
                result = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
                # # print(result)
        return int(stack[0])

