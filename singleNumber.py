class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1    
        for key in dict:
            if(dict[key] == 1):
                return key
