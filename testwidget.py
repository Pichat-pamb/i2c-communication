import tkinter as tk

def display_color():
    color_code = entry.get()  # Get the color code from the entry widget
    try:
        # Create a new window and set its background color to the input color code
        window = tk.Toplevel()
        window.configure(background=color_code)
        window.title("Color Display")
        window.geometry("200x200")
        window.mainloop()
    except tk.TclError:
        # If an invalid color code is entered, show an error message
        error_label.config(text="Invalid color code", fg="red")

# Create the main window
root = tk.Tk()
root.title("Color Display Program")

# Create the entry widget for color code input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to display the color
display_button = tk.Button(root, text="Display Color", command=display_color)
display_button.pack()

# Create a label for error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=10)

root.mainloop()