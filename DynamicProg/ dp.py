# It is just a buzzword
# it helps in optimization using cacheing
# Dp helps to solve a complex problem by breaking it into small sub problems 
# and solving the sub problems only once and storing their solutions in case the same problems occur


# Caching is way to store values like a backpack that we can take to school
# Memonization is a specific for of caching
# Suppose ek kaam ho baar baar karna hai jo bhot time leta hai execute hone mai
# 
# We first create a Cache = {} and a function    

# Checklist if we can solv by DP

# 1) Can be divided into subproblem -- Tree like
# 2) Recursive solution -- divide kar sakte hai
# 3) Are there repetetive problems -- yes
# 4) Memoize sub problems --

def add80 (n) : 
    return n+80


# Cache = {} # we  dont pollute the global environment so avoid global scope
# This outer function will be called ONCE to set up the cache and return the helper function.
def memonizedAddto80():
    # Initialize Cache: This line runs only ONCE when memonizedAddto80() is called.
    Cache = {} # we mention it here
    # 2. Define the Helper: This inner function is a 'closure'. 
    # It remembers and continues to use the 'Cache' variable from the outer function's scope.
    def helper(n):
        if n in Cache:
            print('It is o(1) time now')
            return Cache[n]
        else:
            print('So much execution')
            Cache[n] = n + 80
            print(Cache)
            return Cache[n]

    return helper
    # 3. Return the Helper function: We return the function itself, not its result.

if __name__ == '__main__':
    print(add80(4)) # This function i want to ache as i will be using this multiple times
    # Setup Memoization (memonized variable now holds the 'helper' function)
    memonized = memonizedAddto80()
    print(memonized(4))
    print(memonized(5)) # Memoization is basically caching return value of a function based on its parameters
    print(memonized(5))
