a=list(map(int,input("Enter the Data:: ").split()))
for i in range(0,len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


#TIME COMPLEXITY ===================== ORDER OF N SQUARE O(n)^2