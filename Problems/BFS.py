# my_list.insert(0, new_element) for insterting at start used when reverse traversal is asked

def bfs_list(graph, start_node):
    """
    Performs BFS traversal using a standard Python list as the queue.
    NOTE: This is less efficient than using collections.deque.
    """
    # 1. Initialize the queue using a standard list.
    queue = [start_node]

    # 2. Initialize the set for visited nodes.
    visited = {start_node}

    # 3. Initialize the list for the traversal order.
    traversal_order = []

    # 4. Loop as long as the queue is not empty.
    while queue:
        # a. Dequeue the current node by popping from the LEFT/FRONT (index 0).
        #    This O(N) operation is the performance bottleneck.
        current_node = queue.pop(0) 

        # b. Add the node to the result.
        traversal_order.append(current_node)

        # c. Explore neighbors.
        for neighbor in graph.get(current_node, []):
            # d. If unvisited:
            if neighbor not in visited:
                # i. Mark as visited.
                visited.add(neighbor)
                # ii. Enqueue the neighbor (add to the RIGHT/END).
                queue.append(neighbor) 
                
    return traversal_order

# from collections import deque
# queue = deque([root])
    # node = queue.popleft()
  # queue.append(node.left)

# Level Order Traversal with Grouping (Conceptual Code)
# queue = deque([root])
# result = []
# while queue: # WE NEED ONLY 1 LOOP FOR NORMAL TRAVERSAL, BUT WHEN CONCERNED REGARDING THE LEVELS WE USE 2
#     level_size = len(queue)  # Key Step 1: Count nodes at this level
#     current_level_elements = []
    
#     # Key Step 2: The for loop iterates ONLY over the nodes counted above
#     for _ in range(level_size):
#         node = queue.popleft()
#         current_level_elements.append(node.val)
#         # Add children (for the NEXT level)
#         if node.left: queue.append(node.left)
#         if node.right: queue.append(node.right)
        
#     result.append(current_level_elements)


# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
# function findSuccessor(root, key) {
#   if (root == null) return null;

#   //initialize the queue with root
#   const queue = [root];

#   while (queue.length > 0) {
#     //get next node
#     const currNode = queue.shift();

#     //insert the children of current node in the queue
#     if (currNode.left !== null) {
#       queue.push(currNode.left);
#     }
#     if (currNode.right !== null) {
#       queue.push(currNode.right);
#     }

#     // break if we have found the key
#     if (currNode.value === key) break;
#   }
#   if (queue.length > 0) return queue.shift();

#   return null;
# }
from collections import deque

class Node:
    """A simple class to represent a binary tree node."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findSuccessor(root: Node, key: int) -> Node:
    """
    Finds the level order successor of the node with the given key.

    Args:
        root: The root node of the binary tree.
        key: The value of the node whose successor is to be found.

    Returns:
        The level order successor Node, or None if the key is not found 
        or is the last node in the level order traversal.
    """
    if root is None:
        return None

    # Initialize the queue with the root. deque is efficient for queue operations.
    queue = deque([root])

    # Flag to track if the key has been found in the previous iteration
    key_found = False

    while queue:
        # Get the next node from the front of the queue
        currNode = queue.popleft()

        # If the key was found in the previous iteration, the current node 
        # is the successor.
        if key_found:
            return currNode

        # Insert the children of the current node into the queue
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)

        # Check if the current node is the key node
        if currNode.value == key:
            # Set the flag to True. The node popped in the NEXT iteration 
            # will be the successor.
            key_found = True
    
    # If the loop finishes (meaning the key was either not found or 
    # was the very last node processed), return None.
    return None

# -----------------
# Example Usage:
# -----------------
# Tree Structure:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Level Order Traversal: 1, 2, 3, 4, 5

# 1. Successor of 2 should be 3
successor_2 = findSuccessor(root, 2)
print(f"Successor of 2: {successor_2.value if successor_2 else None}") # Output: 3

# 2. Successor of 3 should be 4
successor_3 = findSuccessor(root, 3)
print(f"Successor of 3: {successor_3.value if successor_3 else None}") # Output: 4

# 3. Successor of 5 (last node) should be None
successor_5 = findSuccessor(root, 5)
print(f"Successor of 5: {successor_5.value if successor_5 else None}") # Output: None
  
# Left View
  
# function treeRightView(root) {
#   let result = [];
  
#   if(root === null) {
#     return result
#   }
  
#   const queue = [root]
  
#   while(queue.length > 0) {
#     let levelSize = queue.length
    
#     for(let i = 0; i < levelSize; i++) {
#       let currentNode = queue.shift()
      
#       //if it is the first node of this level,
#       //add it to the result
#       if(i === 0){
#         result.push(currentNode.value)
#       }
#       //insert the children of current node in the queue
#       if(currentNode.left !== null) {
#         queue.push(currentNode.left)
#       }
#       if(currentNode.right !== null) {
#         queue.push(currentNode.right)
#       }
#     }
#   }

#   return result;
# };


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # We'll use a list/array to simulate passing variables by reference 
        # in Python (or you could use class attributes like you tried).
        self.k = k
        self.count = 0
        self.result = None
        
        def inorder_traversal(node):
            # If we've already found the result, stop recursing
            if not node or self.result is not None:
                return

            # 1. Traverse Left (Left subtree contains smaller elements)
            inorder_traversal(node.left)
            
            # If result is already found during the left traversal, immediately return
            if self.result is not None:
                return
            
            # 2. Visit Root (Count the current node)
            self.count += 1
            
            if self.count == self.k:
                # This is the k-th smallest element! Store the value and stop.
                self.result = node.val
                return
            
            # 3. Traverse Right (Right subtree contains larger elements)
            inorder_traversal(node.right)

        inorder_traversal(root)
        return self.result


# Kthe smallest elemnt from binary tree wala result
