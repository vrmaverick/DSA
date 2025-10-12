# To find Ceiling ---- Return start , to find floor ---- return end

# function searchCeilingOfNumber(arr, key) {
#   const n = arr.length 
#   let start = 0;
#   let end = n - 1;
  
#   if (key > arr[end]) {
#     return -1;
#   }
  
#   while (start <= end) {
#     let mid = Math.floor(start + (end - start) / 2);
    
#     if (arr[mid] > key) {
#         // key is in first half
#         end = mid - 1;
#       } else if (arr[mid] < key) {
#         //key is in second half
#         start = mid + 1;
#       } else {
#         //found the key
#         return mid
#       }
#   }
  
#   // since the loop is running until 'start <= end', so at the end of the while loop, 'start === end+1'
#   // we are not able to find the element in the given array, so the next big number will be arr[start]
#   return start;
# }
