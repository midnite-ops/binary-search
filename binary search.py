#!/usr/bin/env python
# coding: utf-8

# # Write a python program for a binary search

# In[1]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Test cases
print(binary_search([1, 2, 3, 5, 8], 6))  # Output: False
print(binary_search([1, 2, 3, 5, 8], 5))  # Output: True


# # Write a Python program to calculate the value of 'a' to the power 'b'.

# In[2]:


def power(a, b):
    return a ** b

# Test case
print(power(3, 4))  # Output: 81
""


# #  Write a Python program to sort a list of elements using the bubble sort algorithm.
# 

# In[3]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in a pass
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

    return arr

# Sample Data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print("Original:", data)
sorted_data = bubble_sort(data.copy())  # Using copy() to avoid modifying the original list
print("Sorted:", sorted_data)


# # Write a Python program to sort a list of elements using the merge sort algorithm.
# 
# 

# In[4]:


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Sample Data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print("Original:", data)
sorted_data = merge_sort(data.copy())  # Using copy() to avoid modifying the original list
print("Sorted:", sorted_data)


# #  Write a Python program to sort a list of elements using the quick sort algorithm.

# In[5]:


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Sample Data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print("Original:", data)
quick_sort(data, 0, len(data) - 1)
print("Sorted:", data)


# In[ ]:




