def selectionSort(array):
    for i in range(0,len(array)):
        minimum=array[i]
        for j in range(i+1,len(array)):
            if array[j] < minimum:
                minimum=array[j]
        array.remove(minimum)
        array.insert(i,minimum)
    return array
