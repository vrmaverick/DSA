x = 0
y= 1
def fibo(x=0,y=1,n=0):
    print(n)
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        print(x,y)
        x,y = y,x+y
        return fibo(x,y,n-1)

def alternate(n):
    # print(n)
    if n < 2:
        return n
    return alternate(n-1) + alternate(n-2)

if __name__ =='__main__':
    num = fibo(x,y,13) #counting from 1
    print(f'Number is : {num}')

    num2 = alternate(12) #counting from 0
    print(f'Number is : {num2}')

# Time complexity is very bad in this case O(2^N) while iterative approach O(n)
# it is good to use recursion if you dont have anything fixed depth ki kab tak jaayega
# Use recusrsion for earching and traversing also sometimes in sorting over iteration
### Everytime using a tree or considering a tree use recursion

### brea larger problem into smaller problems each subproblem is identical and the solutions are later combined 
