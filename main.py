import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
from tkinter import messagebox as mb
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sorting_algorithms import bucket_sort,bubble_sort, countingSort, insertion_sort, quick_sort, radix_sort, heap_sort, quick_select

class SortingApp:
    def __init__(self, root):
        # Initialize the main application
        self.root = root
        self.root.title("Sorting Algorithm Analysis")
        self.k_value = None # for quick select algorithm
        self.array_temp = []
       
        self.input_frame = ttk.Frame(root)  # Frame for Input Elements
        self.graph_frame = ttk.Frame(root)  # Frame for Bar Chart

        # UI Elements in the input frame
        self.random_array_button = ttk.Button(self.input_frame, text="Generate Random Array", command=self.generate_random_array)
        self.array_label = ttk.Label(self.input_frame, text="Array Values (comma-separated):")
        self.array_entry = ttk.Entry(self.input_frame)
        self.algorithm_label = ttk.Label(self.input_frame, text="Select Sorting Algorithms:")

        # variables to store checkboxes results
        self.bubble_sort_var = tk.IntVar()
        self.counting_sort_var = tk.IntVar()
        self.insertion_sort_var = tk.IntVar()
        self.quick_sort_var = tk.IntVar()
        self.bucket_sort_var = tk.IntVar()
        self.heap_sort_var = tk.IntVar()
        self.radix_sort_var = tk.IntVar()
        self.quick_select_var = tk.IntVar()

        # Checkboxes
        self.bubble_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Bubble Sort", variable=self.bubble_sort_var)
        self.counting_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Counting Sort", variable=self.counting_sort_var)
        self.insertion_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Insertion Sort", variable=self.insertion_sort_var)
        self.quick_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Quick Sort", variable=self.quick_sort_var)
        self.bucket_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Bucket Sort", variable=self.bucket_sort_var)
        self.heap_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Heap Sort", variable=self.heap_sort_var)
        self.radix_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Radix Sort", variable=self.radix_sort_var)
        self.quick_select_checkbox = ttk.Checkbutton(self.input_frame, text="Quick Select", variable=self.quick_select_var, command=self.prompt_k_value)
        
        self.run_button = ttk.Button(self.input_frame, text="Run", command=self.run_algorithms)         # Button to run sorting algorithms

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)

        # Pack UI Elements in the input frame
        self.array_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.array_entry.grid(row=0, column=1, columnspan=5, padx=5, pady=5, sticky="we")
        self.random_array_button.grid(row=0, column=6, columnspan=2, padx=5, pady=5, sticky="we")

        self.algorithm_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.bubble_sort_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.counting_sort_checkbox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.insertion_sort_checkbox.grid(row=3, column=2, padx=40, pady=5, sticky="w")
        self.quick_sort_checkbox.grid(row=3, column=3, padx=40, pady=5, sticky="w")
        self.bucket_sort_checkbox.grid(row=3, column=4, padx=40, pady=5, sticky="w")
        self.heap_sort_checkbox.grid(row=3, column=5, padx=40, pady=5, sticky="w")
        self.radix_sort_checkbox.grid(row=3, column=6, padx=40, pady=5, sticky="w")
        self.quick_select_checkbox.grid(row=3, column=7, padx=40, pady=5, sticky="w")
        self.run_button.grid(row=4, column=0, columnspan=8, pady=10)

        self.input_frame.pack(side="top", fill="x", padx=10, pady=10) # Pack the input frame at the top

        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=3, columnspan=2, padx=5, pady=5, sticky="nsew") # Configure the grid for the graph in the graph frame
        self.canvas.draw()

        self.graph_frame.pack(side="bottom", fill="both", expand=True) # Pack the graph frame at the bottom

        root.geometry("1920x1080")  # Adjust the size as needed

        root.grid_columnconfigure(0, weight=1) # Configure the column to expand horizontally

        self.graph_frame.grid_propagate(False)
        self.graph_frame.grid_rowconfigure(0, weight=1)  # frame expands vertically
        self.graph_frame.grid_columnconfigure(0, weight=1)  # frame expands horizontally

    def generate_random_array(self):
        try:

            size = sd.askinteger("Random Array Size", "Enter the size of the array(10-50):") # Prompt the user to enter the size of the array

            if size is None: # Check if the user pressed cancel
                return
            if size > 50 or size < 10:
                mb.showerror("Invalid Input", "Please enter the size within the mentioned range!")
            
            random_array = [random.randint(1, 100) for _ in range(size)] # Generate a random array of the specified size

            
            self.array_entry.delete(0, tk.END) # Fill the array entry with the generated array
            self.array_entry.insert(0, ', '.join(map(str, random_array)))

        except ValueError:
            mb.showerror("Invalid Input", "Please enter a valid integer for the array size.")
    
    def prompt_k_value(self):
        if self.quick_select_var.get() == 1:
            self.get_k_value()

    def get_k_value(self):
        try:
            self.k_value = sd.askinteger("Kth Value", "Enter the value of k for Quick Select:")
            if self.k_value is None:
                return
            return self.k_value
        except ValueError:
            mb.showerror("Invalid Input", "Please enter a valid integer for the k value.")


    def run_algorithms(self):
        # Get user inputs

        array_values = [int(val.strip()) for val in self.array_entry.get().split(',')]

        # input_values = self.array_entry.get().split(',')
        # array_values = [int(input_values[0].strip())]  # Store the first value
        # array_values.extend([int(val.strip()) for val in input_values[1:] if int(val.strip()) < 0])
        
        self.array_temp = array_values
        if self.k_value:
            if self.k_value < 1 or self.k_value > len(array_values):
                mb.showerror("Invalid Input", "Please enter a k value > 0 and less than length of array")
                return None
            

        
        # Store selected algorithms
        selected_algorithms = {
            'Bubble Sort': self.bubble_sort_var.get(),
            'Counting Sort': self.counting_sort_var.get(),
            'Insertion Sort': self.insertion_sort_var.get(),
            'Bucket Sort': self.bucket_sort_var.get(),
            'Quick Sort': self.quick_sort_var.get(),
            'Heap Sort': self.heap_sort_var.get(),
            'Radix Sort': self.radix_sort_var.get(),
            'Quick Select': self.quick_select_var.get()
        }


        algorithm_runtimes = {}
        print(array_values)
        if selected_algorithms['Bubble Sort']:
            algorithm_runtimes['Bubble Sort'] = self.measure_runtime(bubble_sort, array_values.copy(), 0)
        if selected_algorithms['Counting Sort']:
            algorithm_runtimes['Counting Sort'] = self.measure_runtime(countingSort, array_values.copy(), 0)
        if selected_algorithms['Insertion Sort']:
            algorithm_runtimes['Insertion Sort'] = self.measure_runtime(insertion_sort, array_values.copy(), 0)
        if selected_algorithms['Bucket Sort']:
            algorithm_runtimes['Bucket Sort'] = self.measure_runtime(bucket_sort, array_values.copy(), 0)
        if selected_algorithms['Quick Sort']:
            algorithm_runtimes['Quick Sort'] = self.measure_runtime(quick_sort, array_values.copy(), 1)
        if selected_algorithms['Heap Sort']:
            algorithm_runtimes['Heap Sort'] = self.measure_runtime(heap_sort, array_values.copy(), 0)
        if selected_algorithms['Radix Sort']:
            algorithm_runtimes['Radix Sort'] = self.measure_runtime(radix_sort, array_values.copy(), 0)
        if selected_algorithms['Quick Select']:
            algorithm_runtimes['Quick Select'] = self.measure_runtime(quick_select, array_values.copy(),2)


        self.display_graph(algorithm_runtimes)

    def display_graph(self, algorithm_runtimes):
        
        self.ax.clear() # Clear the existing graph

        algorithms = list(algorithm_runtimes.keys()) # Extract algorithm names and runtimes
        runtimes = [runtime[0] for runtime in algorithm_runtimes.values()]

        colors = ['cyan', 'lightblue', 'lightgreen', 'tan', 'royalblue', 'sandybrown', 'salmon', 'pink'] # Set colors for the bars
        
        self.ax.bar(algorithms, runtimes, color=colors[:len(algorithms)],edgecolor='black', linewidth=1) # Create a bar graph
        self.ax.set_xlabel('Sorting Algorithms')
        self.ax.set_ylabel('Runtime')
        self.ax.set_title('Sorting Algorithm Runtimes')

        if len(algorithms) > 3:  # Adjust x-axis label formatting if there are more than 3 algorithms
            for label in self.ax.get_xticklabels():
                label.set_fontsize(6)  # Adjust font size as needed

        
        self.canvas.draw()

    def measure_runtime(self,sorting_function, array, flag):
        
        start_time = datetime.now()
        if flag == 1:
            x = sorting_function(array, 0, len(array) - 1)
        elif flag == 2:
            x = sorting_function(array, 0, len(array) - 1, self.k_value)
        else:
            x = sorting_function(array)
        print(sorting_function,x)
        end_time = datetime.now()
        difference = (end_time - start_time).total_seconds()
        return [difference]

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
