from util import time_it

@time_it
def linear_search(number_list, num_to_find):
    for index, element in enumerate(number_list):
        if element == num_to_find:
            return index
    return -1


@time_it    

def binary_search(number_list, num_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]
        
        if mid_number == num_to_find:
            return mid_index
        
        if mid_number < num_to_find:
            left_index = mid_index + 1
            
        
        if mid_number > num_to_find:
            right_index = mid_index -1
            
    return -1

    



number_list = [i for i in range(100000001)]
b = linear_search(number_list, 100005)
print(b)

a = binary_search(number_list, 100005)
print(a)