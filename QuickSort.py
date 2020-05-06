#Function to sort
def split(array,lb,ub):
    start=lb
    end=ub
    pivot=array[lb]
    
    while start < end:
        while array[start] <= pivot:
            start+=1
        while array[end] > pivot:
            end-=1
        if start < end:
            array[start],array[end]=array[end],array[start]
    else:
        array[lb],array[end]=array[end],array[lb]
            
    return end

#Function to divide 
def sort(array,lb,ub):
    if lb < ub:
        pos=split(array,lb,ub)
        sort(array,lb,pos-1)
        sort(array,pos+1,ub)

#GUI function to accept input        
def quickSort(array):
    lb=0
    ub=len(array)-1
    sort(array,lb,ub)
