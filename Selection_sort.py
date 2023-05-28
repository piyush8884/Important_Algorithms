
def selection(inputs):
    for i in range(0,len(inputs)):
        for j in range(i+1,len(inputs)):
            if inputs[i]>inputs[j]:
                inputs[i],inputs[j]=inputs[j],inputs[i]
    return inputs

inputs=list(map(int,input("Enter the List:: ").split()))
print(selection(inputs))