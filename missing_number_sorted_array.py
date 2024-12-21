class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums)-1

        while(start < end):
            mid = (start + end) // 2

            if (nums[mid] - mid - 1) < k:
                start = mid + 1

            else:
                end = mid
        
        return start + k
        