class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_ending_here = 0
        if len(nums)<=5:
            l = len(nums)
            a = []
            for i in range(l):
                summ = 0
                for j in range(i,l):
                    summ+=nums[j]
                    a.append(summ)
            a.sort()        
            return a[-1]
        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_ending_here < 0:
                max_ending_here = 0
         
        
            elif (max_so_far < max_ending_here):
                max_so_far = max_ending_here
             
        return max_so_far
        
            
        
