def merge_sort(A, key, descending = False):
    size = len(A)
    if size == 1:
        return A
    left_array = merge_sort(A[0:size//2], key, descending = False)
    right_array = merge_sort(A[size//2:size], key, descending = False)
    sorted_array = merge(left_array, right_array, key, descending = False)
    
    return sorted_array

def merge(left_array, right_array, key, descending = False):
    sorted = []
    while len(left_array) > 0 and len(right_array) > 0:
        if descending:
            if left_array[0][key] > right_array[0][key]:
                sorted.append(left_array.pop(0))
            else:
                sorted.append(right_array.pop(0))
        else:
            if left_array[0][key] < right_array[0][key]:
                sorted.append(left_array.pop(0))
            else:
                sorted.append(right_array.pop(0))
                
    while len(left_array) > 0:
        sorted.append(left_array.pop(0))
    while len(right_array) > 0:
        sorted.append(right_array.pop(0))
        
    return sorted

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

sorted_list = merge_sort(elements, key='time_hours', descending=True)
print(sorted_list)
            
                

