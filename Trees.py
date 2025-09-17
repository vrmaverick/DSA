#Binary tree mai levels 0----n nodes = 2 raise to n
#Binary trees jo full and complete hoo wo most efficient as leaf nodes = all other nodes above +1
#So traversing only through half of the data
# O(logn) as log of nodes(n) = steps/height of the tree---------1 of several possiblity like divide and concure
# 1) Great for comparing
# 2) used to preserve relationships unlinke hash map
# 3) Flexible and ordered
# 4) better for lookup than array o(logn), insert and delete(shifting) is also slower in arrays
# 5) Arent Fastest in any feild its like sub optimal
# unbalance search tree is bad as sab ek side pe lagte lagte it will look like a linkedlist -- -all operations in worst case also are O(n)

# Balanced BST ko balance karna pafta hai that can get to linear unbalanced tree jab bhot data add karenge toh
# Therefore, AVL trees and Red/Black trees use karna better hai as it auto balances par implementation mushkil hai kuch lubraries use kar ke kar sakte hai

# Heap; Heam hum log tree jaisa hii structure hota hai but for ek order mai add karta hai and min and max ke basis pe upar niche karta hai
# iski order preserve rehthi hai and yeh fast hai insertion mai bas problem is lookup slower hai ek pattern nahi hai isiliye
#but min/max jo root mai rehta hai uska O(1) rehta hai which is good

# Trie : Specialized tree also called prefix tree used for strings. isme letter nodes hote hai like auto complete fatafat sugesstions dega aur iski time complexity and space complecity is the best for strings = > O(len of word)


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


if __name__ == '__main__': 
    bst = BST()
    bst.insert(45)
    bst.insert(18)
    bst.insert(10)
    bst.insert(98)
    bst.insert(56)
    bst.insert(85)
    bst.insert(52)

    bst.remove(45)
    f = bst.lookup(56)
    # print(bst.root)
    print(bst.root.value)
    # print(bst.root.left.value)
    print(bst.root.right.left.value)