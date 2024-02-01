
import tkinter as tk

def generate_graphs():
    pass

def algorithms_codes():
    pass








def get_screen_dimensions(root):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return screen_width, screen_height


root = tk.Tk()
root.title("Algorithm Analysis Tool")

# Set the dimensions of the main window
window_width = 800
window_height = 600
screen_width, screen_height = get_screen_dimensions(root)
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a button to trigger the analysis
recommend_button_font = ("Arial", 24, "bold")
recommend_button = tk.Button(root, text="Start Analysis", font=recommend_button_font, command=algorithms_codes)
recommend_button.grid(padx=10, pady=10)  


root.mainloop()