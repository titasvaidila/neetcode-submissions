class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # impossible if unequal lengths
        if len(s) != len(t):    
            return False

        # at most 26 characters, hence O(1) space complexity
        countS, countT = {}, {}

        # iterates through s and t, hence O(len(s) + len(t)) time complexity
        for i in range(len(s)):
            # if key doesn't exist default value 0, crashes otherwisr
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            # .get used to avoid key error again
            if countS[c] != countT.get(c, 0):
                return False

        return True