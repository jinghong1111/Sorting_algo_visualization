import time
from colors import *

def heapify(rand_arr, n, i, generate_arr_list, timer):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and rand_arr[i] < rand_arr[left]:
        largest = left

    if right < n and rand_arr[largest] < rand_arr[right]:
        largest = right

    if largest != i:
        rand_arr[i], rand_arr[largest] = rand_arr[largest], rand_arr[i]
        heapify(rand_arr, n, largest, generate_arr_list, timer)


def heap_sort(rand_arr, generate_arr_list, timer):
    n = len(rand_arr)

    for i in range(n-1, -1, -1):
        heapify(rand_arr, n, i, generate_arr_list, timer)

    for i in range(n-1, 0, -1):
        rand_arr[i], rand_arr[0] = rand_arr[0], rand_arr[i]
        heapify(rand_arr, i, 0, generate_arr_list, timer)
        generate_arr_list(rand_arr, [YELLOW if x == i else BLUE for x in range(n)])
        time.sleep(timer)
    
    generate_arr_list(rand_arr, [BLUE for x in range(len(rand_arr))])
    