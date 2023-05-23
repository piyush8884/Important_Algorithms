# Linear search

# The Linear search helps us to find the index of a particular number in an array
# In the real world Linear search helps us a lot : for example "Scenario: Finding a book in a library
#
# Suppose you visit a library with numerous books arranged in a linear fashion on the shelves. You want to find a book with a specific title.
#
# Start at the beginning of the shelf.
# Read the title of the first book.
# Compare the title of the current book with the target book title you are searching for.
# If the titles match, you have found the book and can stop searching.
# If the titles do not match, move to the next book on the shelf.
# Repeat steps 3-5 until you either find the book or reach the end of the shelf.
# This process of sequentially checking each book until a match is found or reaching the end of the shelf is an example of a linear search.

#code
def linear(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            index=i
            return index
            break
    else:
        return -1
arr=list(map(int, input("Enter numbers separated by space: ").split()))

key=int(input("Enter the Number to find "))
print(linear(arr,key))