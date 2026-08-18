class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create dict
        #iterate through list
        # if nums[i] - 1 in the dict,
            # increment the value,
            # remove that key, 
            # add the current number as a key and the value incremented by one
        # if not, then add it and a 1 as the value
        # find the max value in the dictionary
        # seen = {}
        # for num in nums:
        #     if (num-1) in seen:
        #         seqcount = seen.pop(num-1) + 1
        #         seen[num] = seqcount
        #     else:
        #         seen[num] = 1
        # curmax = 1
        # for k, v in seen.items():
        #     if v > curmax:
        #         curmax = v
        # return curmax
        # # ^^ apparently this doesn't work bc the sequence can be out of order
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest