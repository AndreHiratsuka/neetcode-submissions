class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                a = stack.pop()
                print(f"a = {a}")
                b = stack.pop()
                print(f"b = {b}")
                soma = int(a) + int(b)
                print(soma)
                stack.append(b)
                stack.append(a)
                stack.append(soma)
                #sum two last ones
            elif op == "D":
                # double previous score
                a = stack.pop()
                stack.append(int(a))
                double = int(a)*2
                print(double)
                stack.append(double)
            elif op == "C":
                stack.pop()
            else:
                stack.append(op)
        total = 0
        for i in range(len(stack)):
            total += int(stack.pop())
            print(f"total = {total}")
        return total