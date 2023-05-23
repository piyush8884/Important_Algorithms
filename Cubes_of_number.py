def cube(n):
    sum=0
    while n>0:
        sum=(sum)+(n%10)*(n%10)*(n%10)
        n=n//10
    return sum
n=int(input("Enter the Number :: "))
k=cube(n)
print(k)


# This Code Shows how to calculate the Cubes of a Number of 3 digit