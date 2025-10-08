# similar to fibonacci 

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n in cache : 
                return cache[n]
            else : 
                if n <= 3 :
                    cache[n] = n
                    return n
                else : 
                    cache[n] = helper(n-1) + helper(n-2)
                    return cache[n]
        return helper(n)  
