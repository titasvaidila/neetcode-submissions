class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map numbers to frequencies
        count = {}
        # Each freq is a list as multiple nums can have the same freq
        freq = [[] for i in range(len(nums) + 1)] 

        # O(n) time + space complexity
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Gets value & freq, each index is a freq and put val there
        # Worst case each num is unique so n items in dic, O(n) time
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # Walk backwards to get most frequent k first
        # At most n elements visited hence O(n) not O(n^2) as usually expected
        # with a nested loop
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
