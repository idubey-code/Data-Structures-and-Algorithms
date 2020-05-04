class PriorityQueue:
#Implementing priority queue using stacks.
    def __init__(self):
        self.element=[]
        self.length=0
        
    def enqueue(self,priority,value):
        newElement={'priority':priority,'value':value}
        if self.length==0:
            self.element.append(newElement)
        else:
            for i in range(self.length):
                if self.element[i]['priority'] >= priority:
                    self.element.insert(i,newElement)
                    self.length+=1
                    return self.element
                
            self.element.append(newElement)
            
        self.length+=1
        return self.element
    
    def dequeue(self):
        if self.length==0:
            return 'Queue is empty'
        else:
            self.element.pop()
            self.length-=1
            return self.element
