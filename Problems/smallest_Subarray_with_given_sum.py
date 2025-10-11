class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0  # Left pointer of the window
        current_sum = 0
        min_length = float('inf')  # Initialize min_length to a very large number
        n = len(nums)

        # R is the right pointer, which expands the window
        for R in range(n):
            # 1. Expand the window by including the element at R
            current_sum += nums[R]
            
            # 2. Contract the window (from the left) while the sum meets the target
            # This is where we find the minimal valid subarray ending at R
            while current_sum >= target:
                # Update the minimal length found so far
                # The current subarray length is R - L + 1
                min_length = min(min_length, R - L + 1)
                
                # Shrink the window by moving L to the right
                # The element nums[L] is removed from the current_sum
                current_sum -= nums[L]
                L += 1
        
        # 3. Return 0 if min_length is still infinity (no such subarray found), otherwise return min_length
        return min_length if min_length != math.inf else 0
