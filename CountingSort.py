def countingSort(array):
    length=len(array)
    array_out=[0]*length
    max_val=max(array)
    count_list=[0]*(max_val+1)
    #Making count array by counting number of elements
    for i in array:
        count_list[i]+=1
    #Updating count array to give actual index
    for i in range(1,len(count_list)):
        count_list[i]=count_list[i]+count_list[i-1]
    #Filling sorted items in second array
    for i in reversed(range(0,length)):
        array_out[count_list[array[i]]-1]=array[i]
        count_list[array[i]]-=1
    for i in range(0,length):
        array[i]=array_out[i]
    del array_out
    return array
