# Selection and bubble sort dono bure hai 2 loops hai so O(n^2) but space complexity linear hai 

def selectionSort(arr):
    for i in range(0,len(arr)):
        # min = arr[i]
        min_index = i
        # print(arr[i])
        for j in range(i,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    print(f"Sorted Array : {arr}")

if __name__ == '__main__':
    array = [4,-5,3,9,7,4,5]
    selectionSort(array)