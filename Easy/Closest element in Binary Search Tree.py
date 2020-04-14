#Problem Statement: https://www.geeksforgeeks.org/find-closest-element-binary-search-tree/

***
The code itself is quite simple to follow. The important thing to note here is that in BST all the values to the left are smaller than the parent, whereas all the value to the right are greater than the parent. 

So, when you check the current node with the target, it will either neglect any one of the side and thereby decreasing the time complexity.

Also, 
Recursive Funtion:
TimeComplexity: O(logN)
SpaceComplexity:O(logN)

Iterative Method:

TimeComplexity: O(logN)
SpaceComplexity:O(1)


***
class newnode:  
  
    # Constructor to create a new node  
    def __init__(self, data):  
        self.key = data  
        self.left = None
        self.right = None
        
        
def ClosestValueInBST(tree, target):
    
     return ClosestValueInBSTRecursive(tree, target, float("inf"))
    
        
    
    
    

def ClosestValueInBSTRecursive(tree, target, closest):
    
    if tree is None:
        return closest
    
    if abs(target - tree.key) < abs(closest - target):
        closest= tree.key
        
    if tree.key > target:
        return ClosestValueInBSTRecursive(tree.left, target , closest)
        
    elif tree.key < target:
        return ClosestValueInBSTRecursive(tree.right, target , closest)
        
    else:
        return closest
    
    
    return closest

def ClosestValueInBSTIterative(tree, target, closest):
    
    if tree is None:
        return closest
        
    currentNode= tree
    
    while currentNode is not None:
        
        if abs(target - currentNode.key) < abs(closest - target):
             closest = currentNode.key
        
        if currentNode.key > target:
            currentNode=currentNode.left
            
        elif currentNode.key < target:
            currentNode=currentNode.right
            
        else:
            break
    
    return closest        
        
        
        
    
    


        
if __name__ == '__main__': 
    root = newnode(9)  
    root.left = newnode(4)  
    root.right = newnode(17) 
    root.left.left = newnode(3)  
    root.left.right = newnode(6) 
    root.left.right.left = newnode(5)  
    root.left.right.right = newnode(7)  
    root.right.right = newnode(22) 
    root.right.right.left = newnode(20)  
    k = 18
    
    #We are first running the entire funtion Recursively.
    print("Recursively")
    print (ClosestValueInBST(root,k))
    print("Iteratively")
    
    print(ClosestValueInBSTIterative(root, k, float("inf")))
        
