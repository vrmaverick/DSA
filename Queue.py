class Node :
    def __init__(self,value):
        self.value = value
        self.next = None


class Queue :  
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.length == 0:
            return None
        return self.first.value
    
    def enqueue (self,value):
        new_node = Node(value)
        if self.length == 0 :
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return self
        
    def dequeue(self):
        if self.length == 0 :
            return self
        else:
            self.first = self.first.next
            self.length -= 1


queue = Queue()
queue.enqueue(78)
queue.enqueue(56)
queue.enqueue(32)
queue.enqueue(89)
queue.enqueue(43)
print(queue.first.value)
print(queue.last.value)
print(queue.peek())
queue.dequeue()
print(queue.peek())
