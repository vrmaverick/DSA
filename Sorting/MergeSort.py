# O(nlogn) ,uses divide and conquer makes it better than O(n^2)
# Recursion
# O(1) for divide
# O (n) to merge
# # stable as it will kep og order in data
# O(n) space complexity 

def MergeSort(array):
    if len(array) == 1 : 
        return array
    arr1 = array[0:round(len(array)/2)]
    arr2 = array[round(len(array)/2):len(array)]
    # print(arr1)
    # print(arr2)

    return merge(
        MergeSort((arr1)),
        MergeSort((arr2))
    )

def merge (left,right):
    i = 0 
    j = 0
    k = 0
    merge = []
    while(i<len(left) and j< len(right)):
        if left[i] >= right[j]:
            merge.append(right[j])
            j += 1
        else:
            merge.append(left[i])
            i += 1
    if i<len(left):
        merge.extend(left[i:]) # to join the lists elements rather append the whole list as 1 element 
    elif j<len(right):
        merge.extend(right[j:])# to join the lists elements rather append the whole list as 1 element
    
    print(merge)


    return merge
if __name__ == '__main__':
    array = [5,9,3,7,6,4,1,2]
    MergeSort(array)