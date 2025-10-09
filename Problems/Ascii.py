class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0

        if len(columnTitle) == 1 :
            return ord(columnTitle)-64

        for char in columnTitle :
            n = (n * 26) + (ord(char)- ord('A') + 1)

        return n
            
# 171. Excel Sheet Column Number
# Easy
# Topics
# premium lock icon
# Companies
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
