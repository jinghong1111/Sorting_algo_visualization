import time
from colors import *

def insertion_sort(rand_arr, generate_arr_list, timer):
    for i in range(len(rand_arr)):
        temp = rand_arr[i]
        k = i
        while k > 0 and temp < rand_arr[k-1]:
            rand_arr[k] = rand_arr[k-1]
            k -= 1
        rand_arr[k] = temp
        generate_arr_list(rand_arr, [YELLOW if x == k or x == i else BLUE for x in range(len(rand_arr))])
        time.sleep(timer)
        
    generate_arr_list(rand_arr, [BLUE for x in range(len(rand_arr))])