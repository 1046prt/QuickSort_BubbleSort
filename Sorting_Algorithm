#Linear_Searching: 
# Defining Searching:
def search(matrix, key):
    found = False
    for i in range(len(matrix)):
        if matrix[i] == key:
            print(f"The key found at cell: {i}")
            found = True
            break
    if not found:
        print("Key Not Found")

# Creation of 1D Array:
matrix = []
size = int(input("Enter the size of 1D Array: "))
for i in range(size):
    matrix.append(int(input(f"Enter element {i + 1}: ")))

# Printing of created Array:
print("The Array is:")
print(matrix)

key = int(input("Enter the key value to search in the array: "))
search(matrix, key)

# Initialize an empty list to store the array elements
arr = []

# Ask the user for the size of the array
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array:")

# Loop to take input for each element in the array
for i in range(n):
    ele = int(input())  # Input an integer element
    arr.append(ele)     # Append the element to the array

#original array
print("The array is:", arr)

# Bubble Sorting 
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n-i-1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr  # Return the sorted array

sorted_arr = bubble_sort(arr)
print("The sorted array is:", sorted_arr)

# Quick Sorting function definition
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choose the pivot element 
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_arr_quick = quick_sort(arr)
print("The sorted array (quick sort) is:", sorted_arr_quick)

# Merge Sorting
def merger_sort():
    def merge(left, right):
        result = []  # List to store merged result
        i = 0  # Index for left array
        j = 0  # Index for right array
        # Loop until we reach the end of either array
        while i < len(left) and j < len(right):
            # Compare elements and append the smaller one to the result
            if left[i] < right[j]:
                result.append(left[i])
                i += 1  # Move to the next element in left
            else:
                result.append(right[j])
                j += 1  # Move to the next element in right
        # Append any remaining elements from both arrays
        result += left[i:]
        result += right[j:]
        return result  # Return the merged array

    # merge_sort
    def merge_sort(arr):
        # Base case: if the array is of length 0 or 1, it's already sorted
        if len(arr) <= 1:
            return arr
        # Find the midpoint and split the array into left and right halves
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])  # Sort the left half
        right = merge_sort(arr[mid:])  # Sort the right half
        return merge(left, right)  # Merge the sorted halves

    
    arr = [5, 2, 9, 1, 7, 6, 3, 8, 4]
    # Call merge_sort and print the sorted array
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    merger_sort()
