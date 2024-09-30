def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0
    k=0

    # Merge the two arrays while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k]=left[i]
            i += 1
        else:
            merged[k]=right[j]
            j += 1
        k+=1

    # Append the remaining elements from left (if any)
    while i < len(left):
        merged[k]=left[i]
        i += 1
        k+=1

    # Append the remaining elements from right (if any)
    while j < len(right):
        merged[k]=right[j]
        j += 1
        k+=1

    return merged

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
