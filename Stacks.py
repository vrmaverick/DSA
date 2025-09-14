class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            # The new node's next pointer points to the old top node
            new_node.next = self.top
            # The new node becomes the new top
            self.top = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        removed_node = self.top
        self.top = self.top.next
        if self.top is None:
            self.bottom = None
        self.length -= 1
        return removed_node.value

print('hi')
stack = Stack()
stack.push(1)
print(stack.peek())
stack.push(2)
print(stack.peek())
stack.push(3)
print(stack.peek())
print(stack.length)

stack.pop()
print(stack.peek())
print(stack.length)

stack.pop()
print(stack.peek())
print(stack.length)

stack.pop()
print(stack.peek())
print(stack.length)