import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result.config(text=password)
    except:
        result.config(text="Enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)
result = tk.Label(root, font="Arial 14")
result.pack(pady=10)

root.mainloop()

