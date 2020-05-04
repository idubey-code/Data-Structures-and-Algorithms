class HashTable:
    def __init__(self,size):
        self.size=size
        self.hash=[None]*size
    
    #Function to generate hash.
    #ord function takes a string of length 1 and return its unicode value. Ex:- a = 97
    def __hash(self,key):
        hashval=0
        for x in range(0,len(key)):
            hashval=(hashval+ord(key[x])*x) % len(self.hash)
        return hashval
        
    def setvalue(self,key,value):
        address=self.__hash(key)
        if self.hash[address]==None:
            self.hash[address]=[]
        self.hash[address].append([key,value])
        return self.hash
    
    def getValue(self,key):
        address=self.__hash(key)
        if self.hash[address]:
            for x in self.hash[address]:
                if x[0]==key:
                    return x[1]
        return 'Undefined'
    
    def keys(self):
        key_list=[]
        for bucket in self.hash:
            if bucket:
                for sub_bucket in bucket:
                    key_list.append(sub_bucket[0])
        return key_list
    
    def values(self):
        value_list=[]
        for bucket in self.hash:
            if bucket:
                for sub_bucket in bucket:
                    value_list.append(sub_bucket[1])
        return value_list
