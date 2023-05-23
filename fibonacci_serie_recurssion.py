# The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones. The series starts with 0 and 1.
#
# Here's the Fibonacci series starting from 0:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#Code:: 1 This one is Using Recurssion
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
n=8
print(fibo(n))
