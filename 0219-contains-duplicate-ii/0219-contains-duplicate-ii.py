class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            # If the number has been seen before
            if num in last_seen:
                # Check if the distance between indices is within k
                if i - last_seen[num] <= k:
                    return True

            # Update the latest index of the current number
            last_seen[num] = i

        return False