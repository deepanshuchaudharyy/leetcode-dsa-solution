class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

# Can also use this Optimal Solution directly i.e
#           return len(nums) != len(set(nums))    ---> return True if contain Duplicate else return False if not contain Duplicate
