
Quick sort 

def quick_sort(arr, low, high):
    # Base case: only sort if the segment has more than one element
    if low < high:
        # 1. DIVIDE: Get the pivot's final, correct index
        pi = partition(arr, low, high) 

        # 2. CONQUER: Recursively sort the left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # PIVOT CHOICE: Use the last element of the segment
    pivot = arr[high]
    i = low - 1  # Index of the smaller element boundary

    # Iterate through the segment (up to, but not including, the pivot)
    for j in range(low, high):
        if arr[j] <= pivot:
            # Found an element smaller than the pivot
            i = i + 1
            # Swap it into the "smaller than pivot" section
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot (arr[high]) into its correct sorted position (i + 1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the pivot's final index
    return i + 1



# FOR SEARCHING KTH LARGEST USING QUICK SORT + pARTION

# 2. The Optimal (QuickSelect/Partitioning) Approach 🚀
# The most efficient way to solve this problem is by using the QuickSelect algorithm, which is based on the same partitioning technique used in QuickSort.

# QuickSelect avoids fully sorting the right or left side of the array that doesn't contain the K 
# th
#   element, leading to better average time complexity.

# Logic:

# Pick a pivot element.

# Partition the array around the pivot, such that all elements less than the pivot are to its left, and all elements greater are to its right.

# If the pivot's final position is exactly the index K−1, then the pivot is the K 
# th
#   smallest element—return it.

# If the pivot's position is less than K−1, the K 
# th
#   smallest element must be on the right side. Recursively search the right subarray.

# Otherwise (if the position is greater than K−1), the K 
# th
#   smallest element must be on the left side. Recursively search the left subarray.

# Time Complexity: O(N) on average. In the worst case (if the pivot selection is always poor), it can degrade to O(N 
# 2
#  ), but this is rare in practice


# function findClosestPoints(points, k) {
#   let result = [];
#   points = points.sort(
#     ([x1, y1], [x2, y2]) =>
#       Math.pow(x1, 2) + Math.pow(y1, 2) - (Math.pow(x2, 2) + Math.pow(y2, 2))
#   );
#   result = [...points.slice(0, k)];

#   return result;
# }
# console.log(
#   `"Here are the k points closest the origin: " ${findClosestPoints(
#     [
#       [1, 2],
#       [1, 3],
#     ],
#     1
#   )}`
# );
# //The Euclidean distance between (1, 2) and the origin is sqrt(5).
# //The Euclidean distance between (1, 3) and the origin is sqrt(10).
# //Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

# console.log(
#   `"Here are the k points closest the origin: " ${findClosestPoints(
#     [
#       [1, 3],
#       [3, 4],
#       [2, -1],
#     ],
#     2
#   )}`
# );
# //[[1, 3], [2, -1]]
