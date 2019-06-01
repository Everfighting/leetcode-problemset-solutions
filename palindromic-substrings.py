#给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
#示例 1:
#
#输入: "abc"
#输出: 3
#解释: 三个回文子串: "a", "b", "c".
#示例 2:
#
#输入: "aaa"
#输出: 6
#说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#注意:
#
#输入的字符串长度不会超过1000。

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        def is_pal_str(x):
            return x==x[::-1]
        n = len(s)
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            for j in range(i,-1,-1):
                if is_pal_str(s[j:i+1]):
                    dp[i]+=1
        return sum(dp)
