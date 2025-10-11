class Solution(object):
    def isPalindrome(self, s):
        """
        Checks if a string is a palindrome using the two-pointer approach.
        Ignores non-alphanumeric characters and is case-insensitive.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # 1. Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            
            # 2. Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 3. Check for mismatch after normalization (lowercasing)
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                
                # 4. Advance both pointers
                left += 1
                right -= 1
        
        # If the loop completes, the string is a palindrome
        return True
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new = []
#         for i in s :
#             if i.isalnum():
#                 new.append(i.lower())
        
        return new == new[::-1]
