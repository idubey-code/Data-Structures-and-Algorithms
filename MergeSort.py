
#Importing sys to use maxsize function
import sys

#GUI function just for input
def mergeSort(array):
    sort(array,0,len(array)-1)

#Function to split array
def sort(array,lb,ub):
        if lb < ub:
            mid=(lb+ub)//2
            sort(array,lb,mid)
            sort(array,mid+1,ub)
            merge(array,lb,mid,ub)

#Function to compare and merge
def merge(array,lb,mid,ub):
    left=array[lb:mid+1]
    right=array[mid+1:ub+1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 0
    for k in range(lb,ub+1):
        if right[j] <= left[i]:
            array[k]=right[j]
            j+=1
        else:
            array[k]=left[i]
            i+=1
