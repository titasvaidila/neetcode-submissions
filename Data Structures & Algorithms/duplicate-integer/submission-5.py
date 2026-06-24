class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_hash = set() # hashmap is more storage efficient than dict, doesn't store pointer to value

        for n in nums: # iterate over list once O(n) time complexity
            if n in num_hash: # check if already exists
                return True
            num_hash.add(n) # O(n) space complexity for full list
        return False
        