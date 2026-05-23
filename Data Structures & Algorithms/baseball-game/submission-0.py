class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == 'D':
                stack.append(2*int(stack[-1]))
            elif op == 'C':
                stack.pop()
            elif op == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(op)
        return sum(int(n) for n in stack)