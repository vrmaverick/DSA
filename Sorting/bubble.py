def bubbleSort(arr):
    n = len(arr)
    # The outer loop iterates through the list
    # The range is from n-1 down to 0, which correctly reduces the sorted part of the list
    for i in range(n - 1, 0, -1):
        print(f"i : {i}")
        # The inner loop iterates up to the current last unsorted element
        for j in range(i):
            print(f"j:{j}")
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
    return arr

if __name__ == '__main__':
    array = [5, 6, 3, 2, 7, 8]
    sorted_array = bubbleSort(array)
    print(sorted_array)
