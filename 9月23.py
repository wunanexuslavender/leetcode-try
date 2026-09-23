#KMP算法的定义了
#见数据结构书



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # 构建next数组
        def build_next(pattern):
            n = len(pattern)
            next_arr = [0] * n
            j = 0  # 指向前缀末尾

            for i in range(1, n):  # i指向后缀末尾
                # 当字符不匹配时，回退j到前一个匹配位置
                while j > 0 and pattern[i] != pattern[j]:
                    j = next_arr[j - 1]

                # 当字符匹配时，j前进
                if pattern[i] == pattern[j]:
                    j += 1

                next_arr[i] = j

            return next_arr

        next_arr = build_next(needle)
        j = 0  # needle的指针

        # KMP匹配过程
        for i in range(len(haystack)):
            # 当字符不匹配时，利用next数组回退
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]

            # 当字符匹配时，j前进
            if haystack[i] == needle[j]:
                j += 1

            # 完全匹配成功
            if j == len(needle):
                return i - j + 1

        return -1




if __name__ == "__main__" :

    sol = Solution()

    haystack = "artyuipokjmnbvcjhgfdsertgbbhjuytdsdcfvghju"
    needle = "sert"

    result = sol.strStr(haystack,needle)

    print("结果",result)
