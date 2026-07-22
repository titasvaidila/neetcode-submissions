class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time requried AND without '/' operator 
        # Multiplying the prefix and postfix of each position gets this

        # doesn't count as extra mem in this problem 
        # static array initialised 
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # start at end and iterate backwards (-1, -1))
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res