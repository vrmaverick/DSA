class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask (all 1s)
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # XOR adds without carry
            sum_ = (a ^ b) & MASK
            # AND + shift calculates carry
            carry = ((a & b) << 1) & MASK

            a, b = sum_, carry

        # If a is negative in 32-bit representation
        return a if a <= MAX_INT else ~(a ^ MASK)


number = 12345
digit_list = list(map(int, str(number)))
print(digit_list) #... convert integers to list



# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp problem, since once reaching a next significant bit for the first time
        # the rest of the counts are the same as previous (all the bit variations leading up to this current significant bit), just offset by the current power of 2

        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]

# Function	Purpose	Example	Output
# bin(decimal_num)	Decimal to Binary	bin(175)	'0b10101111'
# hex(decimal_num)	Decimal to Hex	hex(175)	'0xaf'
# oct(decimal_num)	Decimal to Octal	oct(175)	'0o257'

# my_string = separator.join(my_list) # To join lists with a seperator can be used to convert list to str
        
        return dp
