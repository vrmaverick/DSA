def MemonizationFibo():
    Cache = {}
    def helper(n):
        if n in Cache : 
            return Cache[n]
        elif n <= 2:
            return n
        else :
            print(' Too many steps')
            Cache[n] = helper(n-1)+helper(n-2)  
            print(Cache)
            return Cache[n]

    return helper
if __name__ == '__main__':
    fibo = MemonizationFibo()
    print(fibo(6))
    print(fibo(6))
    print(fibo(6))
    print(fibo(6))