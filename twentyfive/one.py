# Binary Heap 


# all levels are cmlety filled expect the last level

# Min Heap , Max Heap 


# min heap 
# Creation 


# why we need 


# minimum and maximum numbers among the set of numbers in o(N)



#Min Heap --> The Value of Each Node is Less Than or Equal to the Value of Both of its Childeren


#Max Heap --> start with high 



# common Operations


# creation , peak  , Etract Min/ MAx . Traversal , Size of Binary Heap , Size of Binary Heap , Insert Value in Binary Heap , Delete the Entrire Binary Heap 


# using list 

# using refernece or pinter



# leftChild --> cell[2x]
# rightChild --> cell[2x+1]


 # initialise the foxed size input 

# Set size of Binaty Heap to 0


class Heap:
  def __init__(self, size):
    self.custom_list = [None] * (size+1)
    self.heapSize =0
    self.maxSize = size+1


def peekofHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.custom_list[1]
  
def size_of_binryHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.heapSize
  

def level_order(rootNode):
    if not rootNode or rootNode.heapSize == 0:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.custom_list[i])


def heapiftInsertion(rootNode, index, heapType):
  parentIndex = int(index/2)
  if index <=1:
    return
  if heapType == "Min":
    if rootNode.custom_list[index] < rootNode.customList[parentIndex]:
      temp = rootNode.custom_list[index]
      rootNode.custom_list[index] = rootNode.custom_list[parentIndex]
      rootNode.custom_list[parentIndex] = temp
    heapiftInsertion(rootNode, parentIndex, heapType)

  elif heapType == "Max":
    if rootNode.custom_list[index]> rootNode.custom_list[parentIndex]:
      rootNode.custom_list[index] , rootNode.custom_list[parentIndex] = rootNode.custom_list[parentIndex], rootNode.custom_list[index]
    heapiftInsertion(rootNode, parentIndex, heapType)
  


def insertNode(rootNode, nodeValue, heapType):
  if rootNode.heapSize +1 == rootNode.maxSize:
    return "The Binary HEap is Full"
  
  rootNode.custom_list[rootNode.heapSize +1] = nodeValue
  rootNode.heapSize+=1
  heapiftInsertion(rootNode, rootNode.heapSize, heapType)
  return "SucessFul"



def heapifyTreeExtract(rootNode, index, heapType):
  leftIndex = index * 2

  

newBinaryHeap = Heap(5)

insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
level_order(newBinaryHeap)

print("------")

print(peekofHeap(newBinaryHeap))
print(size_of_binryHeap(newBinaryHeap))

#---- Creation
# Time Complexity --> o(1)
# Space Complexity --> o(N)


# size 

## Time Complexity --> o(1)

## Space Complexity --> o(1)

    
