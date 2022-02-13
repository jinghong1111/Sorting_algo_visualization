import time
from colors import *

def merge(rand_arr, start, mid, end, generate_arr_list, timer):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(rand_arr[q])
            q+=1
        elif q > end:
            tempArray.append(rand_arr[p])
            p+=1
        elif rand_arr[p] < rand_arr[q]:
            tempArray.append(rand_arr[p])
            p+=1
        else:
            tempArray.append(rand_arr[q])
            q+=1

    for p in range(len(tempArray)):
        rand_arr[start] = tempArray[p]
        start += 1

def merge_sort(rand_arr, start, end, generate_arr_list, timer):
    '''
    This is a helper function that performs the merging 
    '''
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(rand_arr, start, mid, generate_arr_list, timer)
        merge_sort(rand_arr, mid+1, end, generate_arr_list, timer)

        merge(rand_arr, start, mid, end, generate_arr_list, timer)

        generate_arr_list(rand_arr, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else RED if x > mid and x <=end else PINK for x in range(len(rand_arr))])
        time.sleep(timer)

    generate_arr_list(rand_arr, [PINK for x in range(len(rand_arr))])