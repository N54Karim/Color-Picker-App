import tkinter as tk
from tkinter import colorchooser
import csv

# Function to pick color and update label
def pick_color():
    # Open the color picker dialog
    color_code = colorchooser.askcolor(title="Choose a color")[1]
    
    if color_code:  # Only proceed if the user selects a color
        # Update the label with the selected color
        color_label.config(text=color_code, bg=color_code)
        # Save the selected color
        save_color(color_code)

# Function to save the color to a CSV file
def save_color(color_code):
    # Save the color to a CSV file
    with open('colors.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([color_code])

# Set up the root window
root = tk.Tk()
root.title("Color Picker App")

# Create and place the color picker button
pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=20)

# Create and place the label to display the selected color
color_label = tk.Label(root, text="Selected Color", width=30, height=5)
color_label.pack(pady=20)

# Run the application
root.mainloop()

