def insertionSort(array):
    for i in range(0,len(array)):
        if array[i] < array[0]:
            temp=array[i]
            array.remove(array[i])
            array.insert(0,temp)
        else:
            if array[i] < array[i-1]:
                for j in range(1,i):
                    if array[i]>=array[j-1] and array[i]<array[j]:
                        temp=array[i]
                        array.remove(array[i])
                        array.insert(j,temp)
    return array
