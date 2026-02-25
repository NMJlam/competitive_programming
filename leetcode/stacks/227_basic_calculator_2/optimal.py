class Solution:
    def calculate(self, s: str) -> int:
        s = list(s.replace(" ", ""))
        n = len(s)
        prev, res, curr = 0, 0, 0
        op = "+"
        i = 0
        while i < n:
            c = s[i]
            if c.isnumeric():
                curr = (curr * 10) + int(c)
            if not c.isnumeric() or i == n - 1:
                if op == "+":
                    res += prev
                    prev = curr
                elif op == "-":
                    res += prev
                    prev = -curr
                elif op == "*":
                    prev *= curr
                elif op == "/":
                    prev = int(prev / curr)
                op = c
                curr = 0
            i += 1
        return res + prev
