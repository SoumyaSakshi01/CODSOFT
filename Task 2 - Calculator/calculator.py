import tkinter as tk

def click(event):
    entry.insert(tk.END, event.widget.cget("text"))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 18", width=4, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        if char == "=":
            btn.config(command=calculate)
        elif char == "C":
            btn.config(command=clear)
        else:
            btn.bind("<Button-1>", click)

root.mainloop()

