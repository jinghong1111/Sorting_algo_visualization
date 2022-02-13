import time
from colors import *

def partition(rand__arr, start, end, generate_arr_list, timer):
    i = start + 1
    pivot = rand__arr[start]

    for j in range(start+1, end+1):
        if rand__arr[j] < pivot:
            rand__arr[i], rand__arr[j] = rand__arr[j], rand__arr[i]
            i+=1
    rand__arr[start], rand__arr[i-1] = rand__arr[i-1], rand__arr[start]
    return i-1

def quick_sort(rand__arr, start, end, generate_arr_list, timer):
    if start < end:
        pivot_position = partition(rand__arr, start, end, generate_arr_list, timer)
        quick_sort(rand__arr, start, pivot_position-1, generate_arr_list, timer)
        quick_sort(rand__arr, pivot_position+1, end, generate_arr_list, timer)

        generate_arr_list(rand__arr, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(rand__arr))])
        time.sleep(timer)
        
    generate_arr_list(rand__arr, [BLUE for x in range(len(rand__arr))])