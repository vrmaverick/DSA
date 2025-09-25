def factorial(n) :
    print(n)
    if n <= 2:
        return n
    return n * factorial(n-1)

if __name__ =='__main__':
    ans = factorial(n=5)
    print(f'factorial is {ans}')