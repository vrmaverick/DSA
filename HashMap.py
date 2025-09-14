# Nothing but dictionaries most important
# Hash functions basically turn some key into a fixed legth gibbrish that on further processing leads us to the momory address where the value is stored
# not ordered all the operations are o(1)

#Cons of hashtables : 
#Hash tables mai collision hoo sakta hai because it is not necessary ki vo har baar evenly distribute karega and therefore on collission link list banta hai and wo traverse karna bhot slow hai when dat is too large and collisions are too frequent
# Slowes down with O(n/k k is the hash table size)
# Too handle collsison we can use seperate chaining (linkedlist) or Robbinhood hashing
# searching a particular takes time need to traverse a whole hash table to get a particular key stored in some memory space
#items randomly placed therefore no order on retrival

# type: ignore
def country() :
    print('India is My Country')

def reccuring(arr):
    dict = {}
    for i in range(0,len(arr)):
        print(arr[i])
        if arr[i] in dict :
            return arr[i]
        else:
            dict[arr[i]] = True
    print('NO reccurent value found')
    return -1    

if __name__ =='__main__':
    user = { 
        
        'name' : 'Maverick',
        'university' : 'NEU',
        'program' : 'MSAI',
        'function': country()
    }

    print(user.get('function')) # O(1) #lookup
    user.pop('name') #delete
    print(user)
    user['name'] = 'Vedant' #insert in O(1)
    print(user) # O(1)
    user['university'] = 'Northeastern' #update
    print(user)

    r = reccuring([1,2,3,2])
    print(f"Reccurring value is {r}")