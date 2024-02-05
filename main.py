import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
from tkinter import messagebox as mb
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, radix_sort, heap_sort

class SortingApp:
    def __init__(self, root):
        # Initialize the main application
        self.root = root
        self.root.title("Sorting Algorithm Analysis")

        # Create frames for user inputs and graph display
        self.input_frame = ttk.Frame(root)
        self.graph_frame = ttk.Frame(root)

        # UI Elements in the input frame
        self.random_array_button = ttk.Button(self.input_frame, text="Generate Random Array", command=self.generate_random_array)
        self.array_label = ttk.Label(self.input_frame, text="Array Values (comma-separated):")
        self.array_entry = ttk.Entry(self.input_frame)
        self.algorithm_label = ttk.Label(self.input_frame, text="Select Sorting Algorithms:")

        # Variables to store checkbox states
        self.bubble_sort_var = tk.IntVar()
        self.selection_sort_var = tk.IntVar()
        self.insertion_sort_var = tk.IntVar()
        self.quick_sort_var = tk.IntVar()
        self.merge_sort_var = tk.IntVar()
        self.heap_sort_var = tk.IntVar()
        self.radix_sort_var = tk.IntVar()

        # Checkboxes for selecting sorting algorithms
        self.bubble_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Bubble Sort", variable=self.bubble_sort_var)
        self.selection_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Selection Sort", variable=self.selection_sort_var)
        self.insertion_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Insertion Sort", variable=self.insertion_sort_var)
        self.quick_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Quick Sort", variable=self.quick_sort_var)
        self.merge_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Merge Sort", variable=self.merge_sort_var)
        self.heap_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Heap Sort", variable=self.heap_sort_var)
        self.radix_sort_checkbox = ttk.Checkbutton(self.input_frame, text="Radix Sort", variable=self.radix_sort_var)

        # Button to run sorting algorithms
        self.run_button = ttk.Button(self.input_frame, text="Run", command=self.run_algorithms)

        # Create a Matplotlib figure for displaying the graph
        self.fig, self.ax = plt.subplots()

        # Display the initial empty plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)

        # Pack UI Elements in the input frame
        self.array_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.array_entry.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky="we")
        self.random_array_button.grid(row=0, column=5, columnspan=2, padx=5, pady=5, sticky="we")

        self.algorithm_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.bubble_sort_checkbox.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.selection_sort_checkbox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.insertion_sort_checkbox.grid(row=3, column=2, padx=60, pady=5, sticky="w")
        self.quick_sort_checkbox.grid(row=3, column=3, padx=60, pady=5, sticky="w")
        self.merge_sort_checkbox.grid(row=3, column=4, padx=60, pady=5, sticky="w")
        self.heap_sort_checkbox.grid(row=3, column=5, padx=60, pady=5, sticky="w")
        self.radix_sort_checkbox.grid(row=3, column=6, padx=60, pady=5, sticky="w")
        self.run_button.grid(row=4, column=0, columnspan=8, pady=10)

        # Pack the input frame at the top
        self.input_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Configure the grid for the graph in the graph frame
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=3, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.canvas.draw()

        # Pack the graph frame at the bottom
        self.graph_frame.pack(side="bottom", fill="both", expand=True)

        # Set a fixed size for the Tkinter window
        root.geometry("1920x1080")  # Adjust the size as needed

        # Configure the column to expand horizontally
        root.grid_columnconfigure(0, weight=1)

        # Set a fixed size for the graph frame
        self.graph_frame.grid_propagate(False)
        self.graph_frame.grid_rowconfigure(0, weight=1)  # Ensure that the frame expands vertically
        self.graph_frame.grid_columnconfigure(0, weight=1)  # Ensure that the frame expands horizontally

    def generate_random_array(self):
        try:
            # Prompt the user to enter the size of the array
            size = sd.askinteger("Random Array Size", "Enter the size of the array:")

            # Check if the user pressed cancel
            if size is None:
                return

            # Generate a random array of the specified size
            random_array = [random.randint(1, 100) for _ in range(size)]

            # Fill the array entry with the generated array
            self.array_entry.delete(0, tk.END)
            self.array_entry.insert(0, ', '.join(map(str, random_array)))

        except ValueError:
            mb.showerror("Invalid Input", "Please enter a valid integer for the array size.")

    def run_algorithms(self):
        # Get user inputs
        input_values = self.array_entry.get().split(',')
        array_values = [int(input_values[0].strip())]  # Store the first value
        array_values.extend([int(val.strip()) for val in input_values[1:] if int(val.strip()) < 0])
        
        # Store selected algorithms
        selected_algorithms = {
            'Bubble Sort': self.bubble_sort_var.get(),
            'Selection Sort': self.selection_sort_var.get(),
            'Insertion Sort': self.insertion_sort_var.get(),
            'Merge Sort': self.merge_sort_var.get(),
            'Quick Sort': self.quick_sort_var.get(),
            'Heap Sort': self.heap_sort_var.get(),
            'Radix Sort': self.radix_sort_var.get()
        }

        # Run selected algorithms and measure runtime
        algorithm_runtimes = {}
        
        if selected_algorithms['Bubble Sort']:
            algorithm_runtimes['Bubble Sort'] = measure_runtime(bubble_sort, array_values.copy(), 0)
        if selected_algorithms['Selection Sort']:
            algorithm_runtimes['Selection Sort'] = measure_runtime(selection_sort, array_values.copy(), 0)
        if selected_algorithms['Insertion Sort']:
            algorithm_runtimes['Insertion Sort'] = measure_runtime(insertion_sort, array_values.copy(), 0)
        if selected_algorithms['Merge Sort']:
            algorithm_runtimes['Merge Sort'] = measure_runtime(merge_sort, array_values.copy(), 0)
        if selected_algorithms['Quick Sort']:
            algorithm_runtimes['Quick Sort'] = measure_runtime(quick_sort, array_values.copy(), 1)
        if selected_algorithms['Heap Sort']:
            algorithm_runtimes['Heap Sort'] = measure_runtime(heap_sort, array_values.copy(), 0)
        if selected_algorithms['Radix Sort']:
            algorithm_runtimes['Radix Sort'] = measure_runtime(radix_sort, array_values.copy(), 0)

        # Display the graph
        self.display_graph(algorithm_runtimes)

    def display_graph(self, algorithm_runtimes):
        # Clear the existing graph
        self.ax.clear()

        # Extract algorithm names and runtimes
        algorithms = list(algorithm_runtimes.keys())
        runtimes = [runtime[0] for runtime in algorithm_runtimes.values()]

        # Set colors for the bars
        colors = ['cyan', 'lightblue', 'lightgreen', 'tan', 'royalblue', 'sandybrown', 'salmon']

        # Create a bar graph
        self.ax.bar(algorithms, runtimes, color=colors[:len(algorithms)])
        self.ax.set_xlabel('Sorting Algorithms')
        self.ax.set_ylabel('Runtime (millisecond)')
        self.ax.set_title('Sorting Algorithm Runtimes')

        # Adjust x-axis label formatting if there are more than 3 algorithms
        if len(algorithms) > 3:
            for label in self.ax.get_xticklabels():
                label.set_fontsize(6)  # Adjust font size as needed

        # Redraw the updated plot in the Tkinter window
        self.canvas.draw()

def measure_runtime(sorting_function, array, flag):
    # Measure the runtime of a sorting algorithm
    start_time = datetime.now()
    if flag == 1:
        sorting_function(array, 0, len(array) - 1)
    else:
        sorting_function(array)
    end_time = datetime.now()
    difference = (end_time - start_time).total_seconds()
    return [difference]

# Main
if __name__ == "__main__":
    # Create the Tkinter window
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
