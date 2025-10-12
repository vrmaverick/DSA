# to fin 1 path

# class TreeNode {
#   constructor(value, left = null, right = null) {
#     this.value = value;
#     this.left = left;
#     this.right = right;
#   }
# }

# function hasPath(root, sum) {
#   if (!root) {
#     return false;
#   }

#   //start DFS with the root of the tree
#   //if the current node is a leaf and it's value is
#   //equal to the sum then we've found a path
#   if (root.value === sum && root.left === null && root.right === null) {
#     return true;
#   }

#   //recursively call to traverse the left and right sub-tree
#   //return true if any of the two recursive calls return true
#   return (
#     hasPath(root.left, sum - root.value) ||
#     hasPath(root.right, sum - root.value)
#   );
# }

#multiple paths ke liye ek list jo all paths store lkare, a list for current path bas end mai back track karna mat bhulna
# PATH KI JABHI JARURAT PADEGI FISRT CALL WITH [] CURRENT_PATH + ALL_PATHS JO KE END MAI STORE HOGA

# function findPaths(root, sum) {
#   let allPaths = []
  
#   findAPath(root, sum, [], allPaths)

#   return allPaths
# };

# function findAPath(currentNode, sum, currentPath, allPaths) {
#   if(currentNode === null) {
#     return
#   }
  
#   //add the current node to the path
#   currentPath.push(currentNode.value)
  
#   //if the current node is a leaf and it's value is 
#   //equal to sum, save the current path
#   if(currentNode.value === sum && currentNode.left === null && currentNode.right === null) {
#     allPaths.push([...currentPath])
#   } else {
#     //traverse the left sub-tree
#     findAPath(currentNode.left, sum - currentNode.value, currentPath, allPaths)
#     //traverse the right sub-tree
#     findAPath(currentNode.right, sum - currentNode.value, currentPath, allPaths)
#   }
  
#   //remove the current node for the path to backtrack,
#   //we need to remove the currentNode while we are going 
#   //up the recursive call stack
#   currentPath.pop()
# }

