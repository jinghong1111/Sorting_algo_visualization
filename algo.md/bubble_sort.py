import time 
from colors import * 

def bubble_sort(rand_arr, generate_arr_list, timer):
    '''
    '''
    size = len(rand_arr)
    for i in range(size - 1 ):
        for j in range(size - i - 1):
            if rand_arr[j] > rand_arr[j+1]:
                rand_arr[j] = rand_arr[j+1]
                rand_arr[j+1] = rand_arr[j]
                generate_arr_list(rand_arr, [YELLOW if x == j 
                or x == j + 1 else PINK for x in range(len(rand_arr))])
                time.sleep(timer)
    generate_arr_list(rand_arr, [PINK for x in range(len(rand_arr))])

