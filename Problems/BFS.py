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
