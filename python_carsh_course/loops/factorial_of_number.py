#in math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
####################
#print the first 10 factorials (from 0 to 9) with the corresponding number

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = x * result
    return result

for n in range(0,10):
    print(n, factorial(n))