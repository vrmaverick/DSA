#  Time Complexity is O(nlogn)
# It has btter space complexity than merge sort.
# O(n^2) is worst case if piviot selected is the smallest or largest


# 1st try, Failed attempt
# def Quicksort(array):
#     if len(array) == 1 :
#         return array
    
#     piviot = array[len(array)-1]
#     i = 0
#     j = len(array)-1
#     while(i != j):
#         if array[i]> piviot:
#             array.append(array[i])
#             array.pop(i)
#             j = j-1
#         else:
#             i=i+1
#     if j != len(array)-1:
#         return(Quicksort(array[0:j].extend(Quicksort(array[j+1:]))))
#     else : 
#         return(Quicksort(array[0:j]))
#         # print(i,j)    
#         # print(array)


def Quicksort_Clean(array):
    # Base Case: List with 0 or 1 element is sorted
    if len(array) <= 1: 
        return array
    
    # 1. Choose Pivot (The last element is a common choice)
    pivot = array[-1]
    
    # 2. Partition using List Comprehensions
    # Create three new lists based on comparison with the pivot
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    # 3. Recursive Call and Concatenation (The FINAL FIX)
    # The return value must be a new list formed by combining the three sorted parts
    # (recursively sorted 'less') + ('equal to pivot') + (recursively sorted 'greater')
    return Quicksort_Clean(less) + equal + Quicksort_Clean(greater)

# Example Usage:

if __name__ == '__main__':
    # Quicksort(array=[4,5,8,1,3])
    array = [4, 5, 8, 1, 3]
    sorted_array = Quicksort_Clean(array)
    print(f"Original: {array}")
    print(f"Sorted: {sorted_array}")