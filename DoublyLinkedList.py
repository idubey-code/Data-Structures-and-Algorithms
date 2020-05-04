class DoublyLinkedList:
    def __init__(self,value):
        self.head={'value':value, 'next':None, 'prev':None}
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
        newNode={'value':value,'next':None, 'prev':None}
        newNode['prev']=self.tail
        self.tail['next']=newNode
        self.tail=newNode
        self.length+=1
        return self.head
    
    def prepend(self,value):
        newNode={'value':value,'next':None,'prev':None}
        self.head['prev']=newNode
        newNode['next']=self.head
        self.head=newNode
        self.length+=1
        return self.head
    
    def insert(self,index,value):
        if index > self.length:
            return self.append(value)
        else:
            newNode={'value':value,'next':None,'prev':None}
            currentNode=self.traverse(index)
            newNode['prev']=currentNode
            nextNode=currentNode['next']
            nextNode['prev']=newNode
            currentNode['next']=newNode
            newNode['next']=nextNode
            self.length+=1
            return self.head
    
    def delete(self,index):
        currentNode=self.traverse(index)
        toBeRemovedNode=currentNode['next']
        nextNode=toBeRemovedNode['next']
        currentNode['next']=nextNode
        nextNode['prev']=currentNode
        self.length-=1
        return self.head
    
    def reverse(self):
        if self.length == 1:
            return self.head
        else:
            currentNode=self.tail
            self.head=self.tail
            
            while currentNode != None:
                temp=currentNode['next']
                currentNode['next']=currentNode['prev']
                currentNode['prev']=temp
                currentNode=currentNode['next']
            
            self.tail=currentNode
            self.head['prev']=None
            
            return self.head
            
