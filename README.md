arr = []
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array:")
for i in range(n):
    ele = int(input())
    arr.append(ele)
print("The array is:", arr)

#Bubble_Sort():
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
sorted_arr = bubble_sort(arr)
print("The sorted array is:", sorted_arr)

#Quick_Sort():
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
sorted_arr_quick = quick_sort(arr)
print("The sorted array (quick sort) is:", sorted_arr_quick)
