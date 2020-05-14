
"""
Input : "14522", k=3 -> 12
        "" , k=5 -> 0
        "123", k=0 -> return 123
        "",k=0 -> 0

Steps:
1. We have option either to include the i digit or exclude the i digit
2. Keeping this in mind , we also have to store answer for small value of k which can be used
afterwards.
3. dp[len(s)][k+1]
4. For  k =0, fill ans= S
5. For k> len(s) ans=0
6. dp[i][j]= min(dp[i-1][j-1],dp[i-1][j]+current_char)
7. return dp[len(s)-1][k]

Giving TLE (above solution)

Lets try basic solution

"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()  
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]     
        return "".join(stack).lstrip("0") or "0"
