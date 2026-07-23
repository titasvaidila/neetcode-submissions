class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Visualise the sequences on a number line, count how
        long each is, convert this to code by turning our
        orignal array into a set and checking if each number has an
        existing neighbour.
        """
        # for checking neighbours exist in O(1) lookup time
        numsSet = set(nums)
        longest = 0

        for i in nums:
            # check if its the start of a sequence
            if (i - 1) not in numsSet:
                length = 0
                # checks current number initially
                while(i + length) in numsSet:
                    length += 1
                longest = max(length, longest)

        return longest
            