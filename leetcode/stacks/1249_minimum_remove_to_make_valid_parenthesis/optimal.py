class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rem_idx = set()
        res = []

        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                stack.pop() if stack else rem_idx.add(i)

        rem_idx.update(set(stack))

        for i, char in enumerate(s):
            if i not in rem_idx:
                res.append(char)

        return "".join(res)
