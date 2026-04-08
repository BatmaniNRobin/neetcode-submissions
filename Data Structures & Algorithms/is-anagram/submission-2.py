class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dihs = {}
        diht = {}

        for chars in s:
            dihs[chars] = 0

        for chars in s:
            dihs[chars] += 1
        
        for chars in t:
            diht[chars] = 0
        
        for chars in t:
            diht[chars] += 1

        if diht == dihs:
            return True
        
        return False