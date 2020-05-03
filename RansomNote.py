class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote in magazine:
            return True
        return False

p1 = Solution()
print(p1.canConstruct("a", "b"))
print(p1.canConstruct("aa", "ab"))
print(p1.canConstruct("aa", "aab"))
            
        