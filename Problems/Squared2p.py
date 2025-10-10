from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the result array of the same size
        result = [0] * n
        
        # Pointers for the input array
        left = 0
        right = n - 1
        
        # Pointer for placing elements in the result array (from back to front)
        write_ptr = n - 1
        
        # Iterate while the two pointers haven't crossed
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            
            # Place the larger squared value at the current position in the result array
            if left_sq > right_sq:
                result[write_ptr] = left_sq
                left += 1  # Move left pointer inward
            else:
                result[write_ptr] = right_sq
                right -= 1 # Move right pointer inward
            
            # Move the write pointer to the next smaller index
            write_ptr -= 1
            
        return result
