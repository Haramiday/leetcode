class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        c = Counter(nums)
        for i in c.keys():
            if c[i]>=2:
                return True
        return False
        
