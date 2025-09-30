# This logic was tough needs some practice

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of the sorted part of the array
        # that are greater than the key one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

    print(f'Sorted Array : {arr}')

if __name__ == '__main__':
    array = [4, 7, 3, 9, 2, 6]
    insertionSort(array)



# Walkthrough with Example [4, 7, 3, 9, 2, 6]
# i = 1:

# key = 7, j = 0.

# while loop condition (7 < 4) is false.

# Array remains [4, 7, 3, 9, 2, 6].

# i = 2:

# key = 3, j = 1.

# while loop:

# 3 < 7? Yes. arr[2] = arr[1] (becomes [4, 7, 7, 9, 2, 6]), j = 0.

# 3 < 4? Yes. arr[1] = arr[0] (becomes [4, 4, 7, 9, 2, 6]), j = -1.

# Loop ends.

# arr[0] (which is j+1) is set to key (3).

# Array becomes [3, 4, 7, 9, 2, 6].

# i = 3: key = 9, j = 2. while loop condition (9 < 7) is false. No change.

# i = 4: key = 2, j = 3.

# 2 < 9? Yes. arr[4] = arr[3] ([3, 4, 7, 9, 9, 6]), j = 2.

# 2 < 7? Yes. arr[3] = arr[2] ([3, 4, 7, 7, 9, 6]), j = 1.

# 2 < 4? Yes. arr[2] = arr[1] ([3, 4, 4, 7, 9, 6]), j = 0.

# 2 < 3? Yes. arr[1] = arr[0] ([3, 3, 4, 7, 9, 6]), j = -1.

# Loop ends.

# arr[0] is set to key (2).

# Array becomes [2, 3, 4, 7, 9, 6].

# The process continues until the array is fully sorted.    