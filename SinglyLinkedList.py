class LinkedList:
    def __init__(self,value):
        self.head={'value':value, 'next':None}
        self.tail=self.head
        self.length=1
        
    def printList(self):
        myList=[]
        currentNode=self.head
        while currentNode != None:
            myList.append(currentNode['value'])
            currentNode=currentNode['next']
        return myList
    
    def traverse(self,index):
        currentNode=self.head
        count=0
        while count!=index-1:
            currentNode=currentNode['next']
            count+=1
        return currentNode
        
    def append(self,value):
        newNode={'value':value,'next':None}
        self.tail['next']=newNode
        self.tail=newNode
        self.length+=1
        return self.head
    
    def prepend(self,value):
        newNode={'value':value,'next':None}
        newNode['next']=self.head
        self.head=newNode
        self.length+=1
        return self.head
    
    def insert(self,index,value):
        if index > self.length:
            return self.append(value)
        else:
            newNode={'value':value,'next':None}
            currentNode=self.traverse(index)
            nextNode=currentNode['next']
            currentNode['next']=newNode
            newNode['next']=nextNode
            self.length+=1
            return self.head
    
    def delete(self,index):
        currentNode=self.traverse(index)
        toBeRemovedNode=currentNode['next']
        currentNode['next']=toBeRemovedNode['next']
        self.length-=1
        return self.head
    
    def reverse(self):
        if self.head['next']==None:
            return self.head
        
        self.tail=self.head
        first=self.head
        second=self.head['next']

        while(second):
            temp=second['next']
            second['next']=first
            first=second
            second=temp
    
        self.head['next']=None
        self.head=first
        return self.printList()
        
