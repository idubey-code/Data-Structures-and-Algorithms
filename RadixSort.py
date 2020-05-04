def count_sort(array,length,position):

    array_out=[0]*length
    #counting array is fixed size 10 as digits at each place are always between 0 & 9
    count_list=[0]*10
    #Filling count array w.r.t position
    for i in array:
        count_list[(i//position)%10]+=1 #for taking elements position by position
        
    #Updating count array to give actual index
    for i in range(1,len(count_list)):
        count_list[i]=count_list[i]+count_list[i-1] 
    
    #Filling sorted items in second array
    for i in reversed(range(0,length)):
        index=(array[i]//position)%10
        array_out[count_list[index]-1]=array[i]
        count_list[index]-=1
    
    #Copying items into original array
    for i in range(0,length):
        array[i]=array_out[i]
    del array_out
    return array

def radixSort(array):
    length=len(array)
    max_val=max(array)
    position=1

    while (max_val//position) > 0:
        array=count_sort(array,length,position)
        position*=10
        
    return array
