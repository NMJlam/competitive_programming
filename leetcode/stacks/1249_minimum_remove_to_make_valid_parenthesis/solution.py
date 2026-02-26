class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        b = s.find("(")
        n = len(s)
        rem_idx = set()
        res = ""

        # This is not required as it is handled by the else conditional
        for i in range(b + 1):
            if s[i] == ")":
                rem_idx.add(i)

        stack = []
        for i in range(b, n):
            char = s[i]
            if char == "(":
                stack.append(i)
            elif char == ")":
                stack.pop() if stack else rem_idx.add(i)

        rem_idx.update(set(stack))

        # String concatenation is O(N^2), we should be using:
        # res = []
        # for i, char in enumerate(s):
        #   if char not in rem_idx:
        #       res.append(char)
        # return ''.join(res)

        for i, char in enumerate(s):
            if i not in rem_idx:
                res += char

        return res
