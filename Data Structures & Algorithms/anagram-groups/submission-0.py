class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Normal dict but if key doesn't exists creates empty list to avoid key error
        res = defaultdict(list) # charCount : list of Anagrams

        # O(m), m is number of strings
        for s in strs:
            count = [0] * 26 # a . . . z

            # O(n), n is length of longest string
            for c in s:
                count[ord(c) - ord('a')] += 1 # a = 80, b = 81 -> 81 - 80 = 1

            # list cannot be used as keys as mutable, tuples are not
            res[tuple(count)].append(s) 

        return list(res.values())

