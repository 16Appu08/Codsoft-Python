import tkinter as tk
from tkinter import messagebox

def add_work():
    work = entry.get()
    if work:
        listbox.insert(tk.END, (work, False))  # Each task is stored as a tuple (task, completed)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_work():
    selected_work_index = listbox.curselection()
    if selected_work_index:
        listbox.delete(selected_work_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def toggle_completion():
    selected_work_index = listbox.curselection()
    if selected_work_index:
        work, completed = listbox.get(selected_work_index[0])
        listbox.delete(selected_work_index)
        listbox.insert(selected_work_index, (work, not completed))
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_all_work():
    listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_work)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_work)
remove_button.pack(side=tk.LEFT, padx=5)

toggle_button = tk.Button(root, text="Toggle Completion", command=toggle_completion)
toggle_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_work)
clear_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Run the main loop
root.mainloop()
