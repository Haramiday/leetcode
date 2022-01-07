class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]>target and target>0 and first>0:
                    print(nums[j])
                    continue
                else:
                    sec = nums[j]
                    if first+sec == target:
                        return [i,j]
