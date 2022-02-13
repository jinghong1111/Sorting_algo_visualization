import time
from colors import *

def selection_sort(rand_arr, generate_arr_list, timer):
    for i in range(len(rand_arr)-1):
        minimum = i
        for k in range(i+1, len(rand_arr)):
            if rand_arr[k] < rand_arr[minimum]:
                minimum = k

        rand_arr[minimum], rand_arr[i] = rand_arr[i], rand_arr[minimum]
        generate_arr_list(rand_arr, [YELLOW if x == minimum or x == i else PINK for x in range(len(rand_arr))] )
        time.sleep(timer)
        
    generate_arr_list(rand_arr, [BLUE for x in range(len(rand_arr))])