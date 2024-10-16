class Solution(object):
    def containsDuplicate(self, nums):
        sset = set()

        for i in nums:
            sset.add(i)

        if len(sset) == len(nums):
            return False
        else:
            return True
