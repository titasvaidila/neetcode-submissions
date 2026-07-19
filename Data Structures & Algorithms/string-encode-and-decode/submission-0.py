class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i

            # Find delimeter
            while s[j] != "#":
                j += 1
            
            # Extract length of word
            length = int(s[i:j])

            # Grab word based on length
            res.append(s[j + 1 : j + 1 + length])

            # Move main pointer to next chunck
            i = j + 1 + length

        return res