# a=[-5,4,6,-3,4,-1]
def kadanes(inputs):
    current=0
    maxi=inputs[0]
    for i in range(0,len(inputs)):
        current=current+inputs[i]
        if maxi<current:
            maxi=current

        if current<0:
            current=0
    return maxi
inputs=list(map(int,input("Enter the Number:: ").split()))

print("Maximum Sum Subarray",kadanes(inputs))


