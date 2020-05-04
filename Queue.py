class Queue:
#Implementing queue using linked lists.
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    
    def enqueue(self,value):
        newNode={'value':value, 'next':None}
        if self.length == 0:
            self.first=newNode
            self.last=self.first
        else:
            self.last['next']=newNode
            self.last=newNode
        
        self.length+=1
        return self.first
    
    def dequeue(self):
        if self.length == 0:
            return None
        if self.first==self.last:
            self.last=None
            
        holdingNode=self.first
        self.first=self.first['next']
        print('Value removed :' + holdingNode['value'])
        
        self.length-=1
        return self.first
    
    def peek(self):
        return self.first['value']
