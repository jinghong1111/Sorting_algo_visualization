from tkinter import *
from tkinter import ttk
import random 
from colors import * 

# sorting algorithms imports 
from algos.bubble_sort import bubble_sort
from algos.merge_sort import merge_sort

#Using tkinter to create a window 
window = Tk()
window.title("Sorting Algorithms In Action")
window.maxsize(1000, 1000)
window.config(background = SKY_BLUE)

#display the name of the algorithms 
algo_input = StringVar()
#display the list of the names of all the sorts 
algo_names = ['Merge Sort', 'Quick Sort', 'Bubble Sort', 'Insertion Sort', 
'Selection Sort', 'Heap Sort', 'Radix Sort', 'Bucket Sort']

#display the speed choice input 
speed_input = StringVar()
#display the speed choices 
speed_select = ['Very Slow', 'Slow', 'Normal', 'Fast', 'Way too fast']

#storage for random array values 
rand_arr = [] 

def generate_arr_list(rand_arr, color_arr):
    '''
    This function will pick a randomly generated list and illustrate 
    it on the window as rectangles.
    ''' 
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 500
    x_width = canvas_width / (len(rand_arr) + 1)
    offset = 10
    spacing = 2
    norm_arr = [i / max(rand_arr) for i in rand_arr]
    for i in range( len(norm_arr)):
        x0 = i * x_width + offset + spacing
        y1 = canvas_height - norm_arr[i] * 360
        x1 = (i + 1) * x_width + offset
        y0 = 0
        canvas.create_rectangle(x0, y0, x1, y1, fill = color_arr[i])

    window.update_idletasks()

def generate_arr(): 
    '''
    This function will generate an array with random values. 
    '''
    for i in range(100):
        rand_int = random.randint(0, 100)
        rand_arr.append(rand_int) 
    generate_arr_list(rand_arr, [PINK for x in range(len(rand_arr))])

def delete_arr(): 
    '''
    This function will delete the generated arrays (all)
    '''
    #delete all stored array values 
    rand_arr.clear()  
    canvas.delete('all')
    window.mainloop()

def set_speed():
    '''
    This function will let user choose a speed.  
    '''
    if speed_menu.get() == "Very Slow":
        return 1 
    elif speed_menu.get() == "Slow": 
        return 0.5
    elif speed_menu.get() == "Normal": 
        return 0.1 
    elif speed_menu.get() == "Fast":
        return 0.001 
    else:
        return 0.0001

def sort(): 
    '''
    This function allow the user to pick a sorting algorithm to visualize.
    '''
    timer = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(rand_arr, generate_arr_list, timer)
        
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(rand_arr, 0, len(rand_arr)-1, generate_arr_list, timer)

### Start of UI implementation --------------------------------------------------------- ###

UI_frame = Frame(window, width = 1000, height = 500, background = WHITE)
UI_frame.grid(row = 0, column = 0 , padx = 10, pady = 5)

# dropdown selection for sorting algorithms
label_1 = Label(UI_frame, text = 'Algorithm: ', background = WHITE) 
label_1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
algo_menu = ttk.Combobox( UI_frame, textvariable = algo_input, values = algo_names)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown selection for sorting speed 

label_2 = Label(UI_frame, text = "Sorting Speed: ", background = WHITE)
label_2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
speed_menu = ttk.Combobox( UI_frame, textvariable = speed_input, values = speed_select)
speed_menu.grid( row = 1, column = 1, padx = 5, pady = 5)
speed_menu.current(0)

# Buttons 

b1 = Button(UI_frame, text = "Sort", command = sort, background = LIGHT_GRAY)
b1.grid(row = 2, column = 3, padx = 5, pady = 5)

# button for generating array 
b3 = Button(UI_frame, text = "Generate Array", command = generate_arr, background = LIGHT_GRAY)
b3.grid(row = 2, column = 0, padx = 5, pady = 5)

# button for deleting array 
b4 = Button(UI_frame, text = "Delete Array", command = delete_arr, background = LIGHT_GRAY)
b4.grid(row = 2, column = 1, padx = 5, pady = 5)

# canvas to draw our array 
canvas = Canvas(window, width = 800, height = 600, bg = WHITE)
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)




window.mainloop() 







