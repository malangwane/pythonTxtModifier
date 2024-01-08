import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk  # Import ttk for the progress bar

# ... (previous code here) ...
# Function to convert text to hexadecimal
def text_to_hex(input_text):
    return input_text.encode('utf-8').hex()

# Function to convert hexadecimal to text
def hex_to_text(hexadecimal_text):
    try:
        return bytes.fromhex(hexadecimal_text).decode('utf-8')
    except ValueError:
        return None  # Return None if the hexadecimal text is not valid

# Function to remove '0a' and replace it with '0d0a' in text
def remove_and_replace_0a(input_text):
    return input_text.replace('0a', '0d0a')

# Function to handle file selection and processing
def process_files():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    if not os.path.exists(input_folder):
        messagebox.showerror("Error", "Input folder does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = [filename for filename in os.listdir(input_folder) if filename.endswith(".txt")]

    progress_bar["maximum"] = len(file_list)  # Set the maximum value of the progress bar

    for idx, filename in enumerate(file_list):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, f"{filename[:-4]}_modified.txt")

        with open(input_file_path, "r", encoding="latin-1") as input_file:
            text_contents = input_file.read()

        modified_text = remove_and_replace_0a(text_contents)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(modified_text)

        progress_bar["value"] = idx + 1  # Update the progress bar value
        root.update_idletasks()  # Update the tkinter GUI

    messagebox.showinfo("Complete", "Modification of all text files complete.")
    progress_bar["value"] = 0  # Reset the progress bar after completion

# Create the main window
root = tk.Tk()
root.title("Text File Modifier: by Wiseman")

# ... (previous code here) ...
# Input folder entry
input_folder_label = tk.Label(root, text="Select Folder With txt Files:")
input_folder_label.pack()
input_folder_entry = tk.Entry(root)
input_folder_entry.pack()
input_folder_button = tk.Button(root, text="Browse", command=lambda: input_folder_entry.insert(0, filedialog.askdirectory()))
input_folder_button.pack()

# Output folder entry
output_folder_label = tk.Label(root, text="Folder to save files:")
output_folder_label.pack()
output_folder_entry = tk.Entry(root)
output_folder_entry.pack()
output_folder_button = tk.Button(root, text="Browse", command=lambda: output_folder_entry.insert(0, filedialog.askdirectory()))
output_folder_button.pack()

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

# Run the tkinter main loop
root.mainloop()
