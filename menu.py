import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Function to load an image using PIL
def load_image(path):
    try:
        # Load and return the image
        image = Image.open(path)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Function to open an application
def open_application(app_command):
    try:
        subprocess.Popen(app_command, shell=True)
    except FileNotFoundError:
        print(f"Application not found: {app_command}")
    except PermissionError:
        print(f"Permission denied: {app_command}")

# Create the main window
root = tk.Tk()
root.title("AI Link Menu")
root.attributes('-fullscreen', True)

# Set the overall background color
root.configure(bg='grey')

# Create a frame for the title
title_frame = tk.Frame(root, bg='light blue')
title_frame.pack(side=tk.TOP, fill=tk.X)

# Add the title label
title_label = tk.Label(title_frame, text="AI Link Menu", bg='light blue', fg='white', font=("Helvetica", 36, "bold"))
title_label.pack(pady=20)

# Create a frame to hold the buttons and description
button_frame = tk.Frame(root, bg='grey')
button_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

# Create a frame for the text and image
text_image_frame = tk.Frame(root, bg='grey')
text_image_frame.pack(side=tk.RIGHT, padx=50, pady=20, fill=tk.BOTH, expand=True)

# Add the descriptive text label
text_label = tk.Label(text_image_frame, text="My name is Caleel Smith and this is my AI final project, which includes 5 different examples of AI.",
                      bg='grey', fg='white', font=("Helvetica", 24, "bold"), wraplength=450, justify="left")
text_label.pack(pady=(0, 10))  # Add padding between text and image

# Add photo under the introduction text
photo_path = "/Users/caleelsmith/Desktop/Menu/img_4491_720.jpg"
photo = load_image(photo_path)
if photo:
    photo_label = tk.Label(text_image_frame, image=photo, bg='grey')
    photo_label.pack(pady=(10, 20), padx=(20, 0), anchor='e')  # Add padding below the photo
    photo_label.image = photo  # Keep a reference to the image
else:
    print(f"Failed to load photo image at {photo_path}")

# Define the button commands and descriptions
buttons = {
    "Chat Bot AI": ("/Users/caleelsmith/Desktop/Menu/Chatty/Chattybot.py", "A chatbot that uses AI to interact."),
    "Weather App": ("/Users/caleelsmith/Desktop/Menu/Weather App/weather_APP.py", "Displays weather forecasts."),
    "Snake Game": ("/Users/caleelsmith/Desktop/Menu/SnakeGame/snakegame.py", "Classic snake game."),
    "Image Recognition": ("/Users/caleelsmith/Desktop/Menu/Image Recognition/vision.py", "Recognize objects in images."),
    "AI Generate": ("/Users/caleelsmith/Desktop/Menu/AI generate/main.py", "Generate content using AI.")
}

# Function to execute a script or open an application
def run_app(app):
    try:
        print(f"Attempting to open: {app}")
        subprocess.Popen(["python3", app])
    except Exception as e:
        print(f"Failed to open {app}: {e}")
        messagebox.showerror("Error", f"Failed to open {app}: {e}")

# Create buttons and descriptions in a zigzag pattern
row = 0
for name, (command, description) in buttons.items():
    align = 'w' if row % 2 == 0 else 'e'

    # Create button
    button = tk.Button(button_frame, text=name, command=lambda c=command: run_app(c),
                       font=("Helvetica", 18, "bold"), bg='blue', fg='black', width=50, height=3, relief=tk.RAISED, bd=5)
    button.grid(row=row, column=0, padx=20, pady=(15, 0), sticky=align)

    # Create description label with a larger font size
    description_label = tk.Label(button_frame, text=description, bg='grey', fg='white', font=("Helvetica", 14, "bold"))
    description_label.grid(row=row + 1, column=0, padx=20, pady=(0, 35), sticky=align)

    row += 2

# Run the application
root.mainloop()
