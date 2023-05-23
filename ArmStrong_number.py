# what is Armstrong Number ?
# The number which has cube of individual number is equal to the sum of that number
# examples 153 = 1*1*1+5*5*5+3*3*3 =153


def arm(n):
    sum=0
    orig=n
    while n>0:
        sum=(sum)+(n%10)*(n%10)*(n%10)
        n=n//10
    if sum==orig:
        return "This number is Armstrong"
    else:
        return "Sorry this is Not Armstrong"
n=int(input("Enter the Number :: "))
k=arm(n)
print(k)