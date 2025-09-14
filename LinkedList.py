# Why to use linked list ?
# Dynamic arrays mai toh koi issue nahi hai scalablity ka but jab scal badhta hai dynamic arrays sab data dusre block mai shift karte hai jiske vajes se time complexity badhta hai
#O(n)
# Arrays have bad performance in insert and delete
# Hashmaps werent orderd

# nodes = ['Value Head' + 'Pointer Tail'] , null terminated and pointer used in between

# Why Linked Lists

# 1) Linked List have a loose structure insert and delte in middle just some pointers change
# prepend and append = O(1)
#insert delete, lookup = O(n) so how is that better ?

class LinkedList:
    def __init__(self,value):
        nextt = None
        self.head = {
            'value' : value,
            'nextt' : None
        }
        self.tail = self.head # Two refrences as head and tail are pointers
        self.length = 1
    
    def append(self,value):
        nextt = None
        new_node = {
            'value':value,
            'nextt' : None
        }
        self.tail['nextt'] = new_node # Last node ka tail badlo
        self.tail = new_node
        self.length = self.length+1
        return self 
    
    def prepend(self,value):
        nextt = self.head
        new_node = {
            'value':value,
            'nextt' : nextt
        }
        self.head = new_node
        self.length = self.length+1
        return self
    
    def insert(self,value,index) :
        # Handle edge case: invalid index
        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return

        # Handle edge case: insertion at the beginning
        if index == 0:
            self.prepend(value)
            return

        # Handle edge case: insertion at the end
        if index == self.length:
            self.append(value)
            return

        # Create the new node
        new_node = {
            'value': value,
            'next': None
        }

        # Traverse to the node BEFORE the insertion point
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node['nextt']

        # Link the new node into the list
        new_node['nextt'] = current_node['nextt']
        current_node['nextt'] = new_node
        
        # Update the list length
        self.length += 1
        return self
    
    def delete (self,index):
        current_node = self.head
        for _ in range(index-2):
            current_node = current_node['nextt']

        current_node['nextt'] = current_node['nextt']['nextt']
        self.length = self.length-1
        return self

    def reverse(self):
        #[1,2,3,4]

        if self.head['nextt'] == 'None':
            return self.head
        
        first = self.head
        self.tail = self.head
        second = first['nextt']

        while (second) : 
            third = second['nextt']
            second['nextt'] = first
            first = second # ek step aage badhegi window so now first is 2
            second = third
        
        self.head['nextt'] = None
        self.head = first # aakhri element tak

        return self

            


if __name__ == '__main__':
    # obj1 = {'name':'Booya'} # Object created and value stored in memory
    # obj2 = obj1 #just an instance but points to same memory not store it diffrently
    # obj1['name'] = 'Vedant' #chnges in memory will affect both pointers as they point to same location
    # print(obj1)
    # print(obj2)

    # If i delete obj1 still obj2 will point to the same memory location therefore upon updating bj2 later it might change the momory location

    obj = LinkedList(10)
    # print(obj.length)
    obj.append(69)
    obj.append(67)
    obj.append(78)
    obj.append(98)
    obj.append(34)
    obj.append(27)
    # print(obj.tail)
    obj.prepend(53)
    # print(obj.length)
    print(obj.head)
    obj.insert(87,4)
    print(obj.head)
    obj.delete(4)
    print(obj.head)
    obj.reverse()
    print(obj.head)