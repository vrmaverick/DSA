class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 1. Edge Case: If k <= 1, no subarray product can be less than k
        if k <= 1:
            return 0
        
        prod = 1
        left = 0  # L
        ans = 0

        # R is the 'right' pointer, iterating through the array
        for right in range(len(nums)):
            # 2. Expand the window
            prod *= nums[right]
            
            # 3. Shrink the window if the product is too large
            # The 'left' pointer advances to keep the product < k
            while prod >= k:
                # The division is safe because the 'left' pointer can never exceed 'right'
                # within this loop's first execution due to the way 'prod' is updated.
                prod /= nums[left]
                left += 1
                
            # 4. Count subarrays
            # The number of valid subarrays ending at 'right' is the size of the current window: (right - left + 1)
            # This is safe because even if the while loop ran and L > R, (R-L+1) would be 0 or less,
            # which is the correct count of 0, but the 'while' loop logic usually prevents L > R 
            # unless a special case like a 0 in nums is encountered. 
            # In a standard Sliding Window, L will never exceed R if initialized correctly.
            ans += (right - left + 1)
            
        return ans
