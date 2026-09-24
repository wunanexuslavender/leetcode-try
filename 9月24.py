# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         yihuo = 0
#         for i in s + t :
#             yihuo ^= ord(i)
#             #ord获取ASCLL码 'a'对应97
#         if chr(yihuo) == None :
#             return true
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True






if __name__ == "__main__" :
    sol = Solution()

    s = "anagram"
    t = "nagaram"

    result = sol.isAnagram(s,t)

    print("我爱莲华",result)