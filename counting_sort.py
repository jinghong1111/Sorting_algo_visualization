import time
from colors import *

def counting_sort(rand_arr, generate_arr_list, timer):
    n = max(rand_arr) + 1
    count = [0] * n
    for item in rand_arr:
        count[item] += 1
    
    k = 0
    for i in range(n):
        for j in range(count[i]):
            rand_arr[k] = i
            generate_arr_list(rand_arr, [BLUE for x in range(len(rand_arr))] )
            time.sleep(timer)
            k += 1

    generate_arr_list(rand_arr, [BLUE for x in range(len(rand_arr))])