class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        print(len(stack))
        for f in logs:
            if stack and  f == '../':
                stack.pop()
            elif f == './' or f == '../':
                continue
            else:
                stack.append(f)
        return len(stack)
