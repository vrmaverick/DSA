if __name__ == '__main__':
     # type: ignore

     # arrays can be static a[5] or dynamic a[] (in python)
     # arrays is used in strings and it is good for sorting, fast lookups, and ordered , however slow insets and delete, and sometimes need to declare the memory (static)
    def Array() : 
        name = ['Vedant', 'Sarvesh', 'Ranade']
        print(name[1])

        # Push #O(1) for static but this can bee O(n) in dynamic arrays
        name.append('Maverick')
        print(name)

        name.pop() # Last by defualt # O(1)
        print(name)

        name.insert(0,'Maverick')
        print(name) # O(n) as we shift the indexes and in middle it will be O(n/2)
    
    def reverse_string(str='vedant'):
        print(str)
        arr = list(str)
        print (len(arr))
        for i in range(0,len(arr)):
            j = len(arr)-1-i
            print(j)
            if i<j:
                temp = arr[i]
                arr[i]= arr[j]
                arr[j] = temp
                print(arr)
            else : 
                pass
    
    def merge_sorted_arrays (arr1= [1,2,3],arr2=[5,6,7]):
        #check inputs
        if not arr1:
            return arr2
        if not arr2:
            return arr1
        for items in arr1:
            if isinstance(items,str):
                print('yes')
                return 0
        for items in arr2:    
            if isinstance(items,str):
                print('yes')
                return 0
        
        merge_sorted_array = []
        print (merge_sorted_array)
        i=0
        j=0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merge_sorted_array.append(arr1[i])
                i += 1
                print (merge_sorted_array)

            else:
                merge_sorted_array.append(arr2[j])
                j += 1
                print (merge_sorted_array)

        
        # After the loop, one array might still have remaining elements.
        # Append all remaining elements from arr1 (if any).
        while i < len(arr1):
            merge_sorted_array.append(arr1[i])
            i += 1
            print (merge_sorted_array)

        
        # Append all remaining elements from arr2 (if any).
        while j < len(arr2):
            merge_sorted_array.append(arr2[j])
            j += 1
            print (merge_sorted_array)

            
        return merge_sorted_array
    
    # merge_sorted_arrays(arr1= [1,8,9],arr2=[5,6,7])
    # reverse_string('Vedant')