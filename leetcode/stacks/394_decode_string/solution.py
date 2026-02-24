class Solution:
    def decodeString(self, s: str) -> str:

        n = 0
        strs = []
        ns = []
        res = ""

        for char in s:
            if char.isdigit():
                n = (n * 10) + int(char)

            elif char == "]":
                x, k = ns.pop(), strs.pop()
                res = k + (x * res)

            elif char == "[":
                ns.append(int(n))
                strs.append(res)
                res = ""
                n = 0

            else:
                res += char

        return res
