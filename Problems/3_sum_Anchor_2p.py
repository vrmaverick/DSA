class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        #Anchor :
        for i in range(n):
            if nums[i]>0:# (-ve walo pe iteration)
                break
            if i > 0 and nums[i] == nums[i-1] :
                continue

            L,R = i+1 , n-1
            target = -nums[i]
                        # Two-Sum on the remainder of the array (O(n) pass)
            while L < R:
                current_sum = nums[L] + nums[R]
                
                if current_sum == target:
                    # Found a triplet
                    result.append([nums[i], nums[L], nums[R]])
                    
                    # Skip duplicates for L
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    # Skip duplicates for R
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    # Move pointers inward to find the next unique pair
                    L += 1
                    R -= 1
                elif  current_sum < target :
                    L += 1
                elif  current_sum > target :
                    R -= 1
        return result
                
