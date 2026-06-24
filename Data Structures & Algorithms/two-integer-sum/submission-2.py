class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prvMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prvMap:
                return [prvMap[diff], i]
            prvMap[n] = i
        return