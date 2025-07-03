import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "Please select a task.")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()
