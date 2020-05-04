class Stack2:
#Implementing stack using arrays.
    def __init__(self):
        self.stack=[]
        self.first=None
        self.last=None
        self.length=0
   
    def push(self,value):
        
        self.stack.append(value)
        self.first=self.stack[0]
        self.last=self.stack[-1]
        self.length+=1
        
        return self.stack
    
    def pop(self):
        
        if self.length == 0:
            return 'Stack is empty.'
        elif self.length == 1:
            self.stack.pop()
            self.first=None
            self.last=None
        else:
            self.stack.pop()
            self.last=self.stack[-1]
        
        self.length-=1
        
        return self.stack
    
    def peek(self):
        return self.last
