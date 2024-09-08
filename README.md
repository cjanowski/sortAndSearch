#Sorting and Searching Algorithms in Python
This repository contains implementations of common sorting and searching algorithms in Python. These implementations are meant for educational purposes and to demonstrate the basic principles of each algorithm.
Algorithms Included
Sorting Algorithms

Bubble Sort

Simple comparison-based algorithm
Time complexity: O(n^2) average and worst case, O(n) best case
Space complexity: O(1)


Quick Sort

Efficient, divide-and-conquer algorithm
Time complexity: O(n log n) average, O(n^2) worst case
Space complexity: O(log n)



Searching Algorithms

Linear Search

Simple search algorithm that checks every element sequentially
Time complexity: O(n)
Space complexity: O(1)


Binary Search

Efficient search algorithm for sorted arrays
Time complexity: O(log n)
Space complexity: O(1)



Usage
To use these algorithms, import them from the algorithms.py file:
pythonCopyfrom algorithms import bubble_sort, quick_sort, linear_search, binary_search

# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list.copy())
print("Sorted list:", sorted_list)

target = 25
index = binary_search(sorted_list, target)
print(f"Index of {target}:", index)
Running the Examples
The algorithms.py file includes example usage for each algorithm. To run these examples, simply execute the file:
Copypython algorithms.py
Contributing
Contributions to improve the implementations or add new algorithms are welcome. Please ensure that any new algorithms are well-commented and include example usage.
License
This project is open source and available under the MIT License.
