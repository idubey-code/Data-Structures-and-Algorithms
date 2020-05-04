def bubbleSort(array):
    for i in range(0,len(array)):
        for j in range(1,len(array)):
            if array[j-1] > array[j]:
                temp=array[j-1]
                array[j-1]=array[j]
                array[j]=temp
    return array
