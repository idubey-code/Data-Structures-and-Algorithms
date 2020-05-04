class MyQueue:
#Implementing queue using stacks.
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
    
    def push(self,value):
        
        for i in range(len(self.out_stack)):
            self.in_stack.append(self.out_stack.pop())
        
        self.in_stack.append(value)
        
        return self.in_stack
    
    def pop(self):
        
        for i in range(len(self.in_stack)):
            self.out_stack.append(self.in_stack.pop())
        
        item=self.out_stack.pop()
            
        return item
    
    def peek(self):
        
        if len(self.out_stack)>0:
            return self.out_stack[-1]
        
        elif len(self.in_stack)>0:
            return self.in_stack[0]
    
    def empty(self):
        if len(self.in_stack)==0 and len(self.out_stack)==0:
            return True
        else:
            return False
