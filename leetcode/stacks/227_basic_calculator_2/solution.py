class Solution:
    def calculate(self, s: str) -> int:

        s = list(s.replace(" ", ""))
        n = len(s)
        num = 0
        op = "+"
        stack = []

        for i, char in enumerate(s):
            if char.isnumeric():
                num = (num * 10) + int(char)

            if not char.isnumeric() or i == n - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "/":
                    prev = stack.pop()
                    res = int(prev / num)
                    stack.append(res)
                elif op == "*":
                    prev = stack.pop()
                    res = prev * num
                    stack.append(res)

                op = char
                num = 0

        return sum(stack)
