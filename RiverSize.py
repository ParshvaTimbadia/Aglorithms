#Problem Statment: https://www.algoexpert.io/questions/River%20Sizes


def RiverSize(matrix):
    sizes=[]
    visited= [[False for value in row ]for row in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if visited[i][j]:
                continue
            
            traverseNode(i,j, matrix, visited, sizes)
    
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    CurrentRiverSize=0
    unvisitedList=[[i,j]]
    
    while len(unvisitedList)!=0:
        currentNode= unvisitedList.pop()
        i= currentNode[0]
        j=currentNode[1]
        
        if visited[i][j]:
            continue
        visited[i][j]==True
        
        if matrix[i][j]==0:
            continue
        
        CurrentRiverSize+=1
        
        univisitedNeighbours = Searchforneighbours(i,j,matrix,visited)
        for neighbours in univisitedNeighbours:
            unvisitedList.append(neighbours)
            
        if CurrentRiverSize>0:
            sizes.append(CurrentRiverSize)

            
    
def Searchforneighbours(i,j,matrix, visited):
    
    unvisited=[]
    if i> 0 and not visited[i-1][j]:
        unvisited.append([i-1,j])
    if i< len(matrix)-1 and not visited[i+1][j]:
        unvisited.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unvisited.append([i, j-1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        unvisited.append([i,j+1])
        
    return unvisited    

if __name__ == '__main__': 
    A= [[1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,0]]
    RiverSize(A)
