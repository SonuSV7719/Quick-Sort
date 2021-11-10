"""
Write a Python profram to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.
"""

# Function to take student percentage:------------------------------------------------

def createArray(n):
    array = []
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        array.append(percentage)
    return array

# Bubble Sort:------------------------------------------------------------

def quickSort(array, start, end):
    if start < end:
        pivot = array[start]
        i = start+1
        j = end
        while True:
            while i<=j and array[i]<=pivot:
                i+=1
            while i<=j and array[j]>=pivot:
                j-=1
            if j<i:
                break
            else:
                array[i], array[j] = array[j], array[i]
        array[start], array[j] = array[j], array[start]
        quickSort(array, start, j-1)
        quickSort(array, j+1, end)
        return array


# Main program start from here -----------------------------------------------------

n = int(input("Enter total number of students value: "))
array = createArray(n)
mini = len(array)-6
maxi = len(array)-1
index = 1
start = 0
end = len(array)-1
array = quickSort(array,start, end )
print("---------------------Top scorer using bubble sort-------------------------\n")
for i in range(maxi, mini, -1):
    if i>=0:
        print(f"Topper No. {index}", array[i],"\n")
    else:
        break
    index+=1   
