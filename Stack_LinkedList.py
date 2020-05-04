class Stack:
#Implementing stack using linked lists.
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    
    def push(self,value):
        newNode={'value':value, 'next':None}
        if self.length == 0:
            self.last=newNode
            self.first=self.last
        else:
            newNode['next']=self.last
            self.last=newNode
        
        self.length+=1
        return newNode
    
    def pop(self):
        if self.length == 0:
            return None
        if self.first==self.last:
            self.first=None
            
        holdingNode=self.last
        self.last=self.last['next']
        print('Value removed :' + holdingNode['value'])
        
        self.length-=1
        return self.last
    
    def peek(self):
        return self.last['value']
    
