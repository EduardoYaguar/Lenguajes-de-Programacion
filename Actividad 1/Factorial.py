from functools import reduce

def Factorial(n):
    if n==0:
        return 1
    else:
        return n * Factorial(n-1)
print(Factorial(3))

def lFactorial(n):

    return reduce(lambda x,y:x*y, range(1,n+1))

print(lFactorial(3))

n = lambda x:1 if x==0 else x* n(x-1)
print(n(3))