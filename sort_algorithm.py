def bubble_sort(number_list):
    size = len(number_list)
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
                swapped = True
        if not swapped:
            break
                
    return number_list



#For Quick sort

def swap(a, b, array):
    if a!=b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp


def partition(element, start, end):
    pivot = start
    pivot_element = element[pivot]
    start = pivot + 1
    end = len(element) - 1
    
    while start < end:
        while element[start] < pivot_element:
            start = start + 1
        
        while element[end] > pivot_element:
            end = end - 1
        
        if start < end:
            swap(start, end, element)
    swap(pivot, end, element)
    return end


def quick_sort(element, start, end):
    if start < end:
        p = partition(element, start, end) 
        quick_sort(element, start, p-1) #left partition
        quick_sort(element, p+1, end) #right partition
    print(element)


element = [11, 2, 9, 7, 15, 29, 28]
e = ["Mona", "Dhaval", "Aamir", "Tina", "Chang"]
#print(bubble_sort(e))   
quick_sort(element, 0, len(element) - 1)