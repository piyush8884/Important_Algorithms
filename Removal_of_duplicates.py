
# TO remove the Duplicates in python either use the Sets or for loop to remove the Duplicacy
list_of_removal=[]
def removal(inputs):
    for i in inputs:
        if i not in list_of_removal:
            list_of_removal.append(i)
    return list_of_removal
inputs=list(map(int,input("Enter ").split()))
print(removal(inputs))