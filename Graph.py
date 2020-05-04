class Graph:
#Implementing graphs using adjacent list.
    def __init__(self):
        self.length=0
        self.adjacentList={}
    
    def addVertex(self,node):
        self.adjacentList[node]=[]
        self.length+=1
        return self.adjacentList
    
    def addEdge(self,node1,node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return self.adjacentList
    
    def showConnections(self):
        keyList=list(self.adjacentList.keys())
        for key in keyList:
            connections=''
            for value in self.adjacentList[key]:
                connections+=value+' '
            print(f'{key} ---> {connections}')
