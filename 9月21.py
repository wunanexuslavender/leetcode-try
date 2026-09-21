#给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
#neywork、




class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        n, m, i, j = len(s1), len(s2), 0, 0
        ans = ""
        while i < n or j < m:
            if i < n:
                ans += s1[i]
                i += 1
            if j < m:
                ans += s2[j]
                j += 1
        return ans

if __name__ =="__main__":
    sol = Solution()

    s1 = "abc"

    s2 = "cdf"

    result = sol.mergeAlternately(s1,s2)
    print("结果",result)