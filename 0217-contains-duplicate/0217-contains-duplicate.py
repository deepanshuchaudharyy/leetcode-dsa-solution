class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A set stores only unique elements.
        # If duplicates exist, the set's size will be smaller than the original list.
            return len(nums) != len(set(nums))