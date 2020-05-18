class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for i in nums:
            if i in a.keys():
                a[i]+=1
                i+=1
            else:
                a[i]=1
                i+=1    
        for key in a:
            if(a[key] == 1):
                return key
