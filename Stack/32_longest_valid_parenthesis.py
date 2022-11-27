class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i-stack[-1])
        return max_length
if __name__ == '__main__':
    s = ")()())"
    ob = Solution()
    ans = ob.longestValidParentheses(s)
    print(ans)