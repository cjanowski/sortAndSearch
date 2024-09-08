# Sorting Algorithms

def bubble_sort(arr):
    """
    Bubble Sort: A simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they're in the wrong order.

    Time complexity: O(n^2) in worst and average cases, O(n) in best case (already sorted)
    Space complexity: O(1)

    :param arr: List to be sorted
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize: if no swaps occur in a pass, the list is already sorted
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    return arr

def quick_sort(arr):
    """
    Quick Sort: An efficient, divide-and-conquer sorting algorithm.
    It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays.

    Time complexity: O(n log n) on average, O(n^2) in worst case
    Space complexity: O(log n) due to recursive calls

    :param arr: List to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    # Partition elements into left (smaller than pivot), middle (equal to pivot), and right (larger than pivot)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)

# Searching Algorithms

def linear_search(arr, target):
    """
    Linear Search: A simple search algorithm that checks every element in the list sequentially.

    Time complexity: O(n)
    Space complexity: O(1)

    :param arr: List to search in
    :param target: Element to search for
    :return: Index of target if found, -1 otherwise
    """
    for i, value in enumerate(arr):
        if value == target:
            return i  # Return index if target is found
    return -1  # Return -1 if target is not in the list

def binary_search(arr, target):
    """
    Binary Search: An efficient search algorithm for sorted arrays.
    It repeatedly divides the search interval in half.

    Time complexity: O(log n)
    Space complexity: O(1)

    :param arr: Sorted list to search in
    :param target: Element to search for
    :return: Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    # Sorting examples
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", unsorted_list)
    print("Bubble sort:", bubble_sort(unsorted_list.copy()))
    print("Quick sort:", quick_sort(unsorted_list.copy()))

    # Searching examples
    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    print("\nSearching for", target, "in", sorted_list)
    print("Linear search result:", linear_search(sorted_list, target))
    print("Binary search result:", binary_search(sorted_list, target))

    # Additional examples
    print("\nSearching for 100 (not in the list):")
    print("Linear search result:", linear_search(sorted_list, 100))
    print("Binary search result:", binary_search(sorted_list, 100))
