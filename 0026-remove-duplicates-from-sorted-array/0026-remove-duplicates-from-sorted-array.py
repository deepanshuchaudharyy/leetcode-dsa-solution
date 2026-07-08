class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0 #initial pointer for unique elements

        #Iteration through the list
        for j in range(1, len(nums)):

            #if the current element is different from previous unique element 
            if nums[i] != nums[j]:
                i+=1 #increase by 1 place
                nums[i] = nums[j] #update the current element with the unique element
        

        return i+1 #return the no. of unique elements