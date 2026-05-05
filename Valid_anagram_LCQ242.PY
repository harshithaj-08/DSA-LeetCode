/*class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)*/
//or
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}
        
        # count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # subtract using t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True
