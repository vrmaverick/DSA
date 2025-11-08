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
