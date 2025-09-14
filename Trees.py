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