# DFS has 3 orders it can return things with

# Inorder 33-101-108 (Ascending order)

    #          110
    #     101      200
    # 33    108 199    201       

Inorder = [33,101,108,110,199,200,201]           
Preorder = [110.101,33,108,200,199,201] # we can recreate a tree easily has the order saved
Postorder = [33,108,101,199,201,200,110]


class Node : 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST : 
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        print(f"New Node ka value {new_node.value}")
        if self.root == None:
            print('----------------------------------------')
            self.root = new_node
            return self
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
            temp = self.root
            print(f"Temp.value : {temp.value}")
            while temp : 
                print(f"Temp.value : {temp.value}")
                if new_node.value == temp.value:
                    print(f"Value {new_node.value} already exists. Skipping insertion.")
                    temp =  0
                if temp.value < new_node.value :
                    prev_node = temp
                    temp = temp.right
                    print(f'New Value of temp 1 :{temp}')
                elif temp.value > new_node.value :
                    prev_node = temp
                    temp = temp.left
                    print(f'New Value of temp 2 :{temp}')

            print(f" While exit and Previous node ka value : {prev_node.value}")
            if prev_node.value < new_node.value:
                prev_node.right = new_node
                print(prev_node.right.value)
            elif prev_node.value == new_node.value:
                print('aready exists')
            else:
                prev_node.left = new_node
                print(prev_node.left.value)

    def lookup(self,value):
        temp = self.root
        while temp :
            if temp.value == value:
                print ('found')
                return True
            elif temp.value < value : 
                temp = temp.right
            else : 
                temp = temp.left
        print('not found')
        return False
    
    def remove(self, value):
        if self.root is None:
            return False  # Tree is empty

        current_node = self.root
        parent_node = None
        
        # Step 1: Find the node to remove and its parent
        while current_node is not None and current_node.value != value:
            parent_node = current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        # If the value was not found
        if current_node is None:
            print(f"Value {value} not found in the tree.")
            return False

        # Step 2: Handle the 3 removal cases
        
        # Case 1: Node to remove has two children
        if current_node.left is not None and current_node.right is not None:
            # Find the inorder successor (smallest node in the right subtree)
            successor = current_node.right
            successor_parent = current_node
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            # Replace current_node's value with the successor's value
            current_node.value = successor.value
            
            # Now, remove the successor (which has at most one child)
            if successor_parent.left is successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        # Case 2: Node to remove has one child
        elif current_node.left is not None or current_node.right is not None:
            child = current_node.left if current_node.left is not None else current_node.right
            if parent_node is None:
                self.root = child
            elif parent_node.left is current_node:
                parent_node.left = child
            else:
                parent_node.right = child
        
        # Case 3: Node to remove has no children (leaf node)
        else:
            if parent_node is None:
                self.root = None
            elif parent_node.left is current_node:
                parent_node.left = None
            else:
                parent_node.right = None
        
        print(f"Successfully removed {value}")
        return True
    
    def BFS(self, value):
        # 3 things required
        current_node = self.root
        list = []
        queue = []
        queue.append(current_node)
        # print(f"Intial queue : {queue}")
        # print(f"Length of queue{len(queue)}")
        while (len(queue) > 0):

            # print(current_node.value)

            if current_node.value == value :
                print("value found")

            current_node = queue[0]
            # print(f"current_node : {current_node}")
            list.append(current_node.value)

            queue = queue[1:]
            # print(queue)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # print(list)        
        return list
    
    def _traverse_inorder(self, node, node_list):
        if node:
            print(node.value)
            self._traverse_inorder(node.left, node_list)
            node_list.append(node.value)
            self._traverse_inorder(node.right, node_list)

    def DFSInorder(self):
        result_list = []
            # Call the helper method using 'self.'
        self._traverse_inorder(self.root, result_list) 
        print (result_list)
        return result_list
    
    def _traverse_preorder(self, node, node_list):
        if node:
            print(node.value)
            node_list.append(node.value)
            self._traverse_preorder(node.left, node_list)
            self._traverse_preorder(node.right, node_list)

    def DFSPreorder(self):
        result_list = []
            # Call the helper method using 'self.'
        self._traverse_preorder(self.root, result_list) 
        print (result_list)
        return result_list
    
    def _traverse_postorder(self, node, node_list):
        if node:
            print(node.value)
            self._traverse_postorder(node.left, node_list)
            self._traverse_postorder(node.right, node_list)
            node_list.append(node.value)

    def DFSPostorder(self):
        result_list = []
            # Call the helper method using 'self.'
        self._traverse_postorder(self.root, result_list) 
        print (result_list)
        return result_list
            


if __name__ == '__main__': 
    bst = BST()
    bst.insert(45)
    bst.insert(18)
    bst.insert(10)
    bst.insert(98)
    bst.insert(56)
    bst.insert(85)
    bst.insert(52)

    # bst.remove(45)
    # f = bst.lookup(56)
    # # print(bst.root)
    # print(bst.root.value)
    # # print(bst.root.left.value)
    # print(bst.root.right.left.value)

    list = bst.DFSInorder()
    list = bst.DFSPreorder()
    list = bst.DFSPostorder()
    # print(list)

 
