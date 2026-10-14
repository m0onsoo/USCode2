class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # initialization
        idx = 0 
        count = 0  # a counter for consecutive occurrences
        prev_num = None  

        for value in nums:
            # track the occurences
            if value == prev_num:  
                count += 1 
            else: 
                prev_num = value 
                count = 1

            # only at most two occurrences are allowed
            if count <= 2: 
                nums[idx] = value  
                idx += 1 

        return idx 