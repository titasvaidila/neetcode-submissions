class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Can't add entire array to hashmap first otherwise we reuse values
        # Max O(n) space complexity
        prevNums = {} # val : index

        # Iterate through array once, so O(n) time complexity
        # Enumerate returns (index, value)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevNums:
                # diff already exists so smaller index and returned first
                return [prevNums[diff], i]
            prevNums[n] = i
        # Not necessary as guaranteed solution
        return

        