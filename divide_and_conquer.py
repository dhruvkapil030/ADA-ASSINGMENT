import time
import random


def binary_search(arr, x, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid-1)
        else:
            return binary_search(arr, x, mid+1, high)
    return -1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]; i+=1
            else:
                arr[k]=R[j]; j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]; i+=1; k+=1
        while j < len(R):
            arr[k]=R[j]; j+=1; k+=1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))
    mid = (low + high)//2
    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid+1, high)
    return max(max1, max2), min(min1, min2)


arr = sorted([random.randint(1,1000) for _ in range(100)])
print("Binary Search:", binary_search(arr, arr[50], 0, len(arr)-1))
