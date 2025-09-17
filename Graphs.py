# most used for modelling real life
# each item is a node and vertex connected with edges
# model relationshsip
# like internet
# there are 2 types directed and in directed graphs

# We first need an edge list
# Usefull for relationships but scaling is really hard as there are many 
# Neo 4J tools used to build complex graphs
# Time and Space complexity difficult to compute




edges = [[0,1],[1,2],[1,3],[1,4],[2,3],[3,4]]

# adjacency matrix , ie index of array is that node itself 
adajency_matrix = [[1], [0,2,3,4],[1,3],[1,2,4],[1,3]] 

# Or 
adajency_matrix = {
    0: [0,1,0,0,0],
    1: [1,0,1,1,1],
    2: [0,1,0,1,0],
    3: [0,1,1,0,1],
    4: [0,1,0,1,0]
}

class graph ():
    def __init__(self):
        self.num_nodes = 0
        self.adjacency_matrix = {}
    
    def AddNode (self,value):
        self.num_nodes += 1
        # The new row is filled with zeros, one for each node (including the new one)
        new_row = [0] * self.num_nodes
        self.adjacency_matrix[value] = new_row
        # We iterate through all rows except the new one and append a zero
        for key in self.adjacency_matrix:
            if key != value:  # Don't add a column to the new node's row just yet
                self.adjacency_matrix[key].append(0)


        print(f"Added node. Matrix is now {self.num_nodes}x{self.num_nodes}.")
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)


    def addEdge(self, vertex, arr):

        if vertex not in self.adjacency_matrix:
            print(f"Error: Vertex {vertex} not found.")
            return False
        for edge in arr:
            if edge not in self.adjacency_matrix:
                print(f"Error: Edge to {edge} not found. Please check your edges.")
                return False

        for edge in arr:
            index = list(self.adjacency_matrix.keys()).index(edge)
            self.adjacency_matrix[vertex][index] = 1

        print(f"Successfully added edges from {vertex} to {arr}")
        return True
        
        

            
        

if __name__ == '__main__':
    network = graph()
    network.AddNode(1)
    network.AddNode(2)
    network.AddNode(3)
    network.addEdge(1,[2,3])
    print(network.adjacency_matrix)