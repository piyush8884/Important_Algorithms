def fibo(n):
    x=0
    y=1
    z=0
    while(z<=n):
        print(z)
        z=x+y
        x=y
        y=z
n=int(input("Enter the number :: "))
fibo(n)

