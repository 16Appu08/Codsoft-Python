import random
import tkinter as tk
from tkinter import messagebox

def generate_weak_password(length):
    ch = "abcdefghijklmnopqrstuvwxyz"
    password = ''.join(random.choice(ch) for _ in range(length))
    return password

def generate_medium_password(length):
    ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choice(ch) for _ in range(length))
    return password

def generate_strong_password(length):
    ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(ch) for _ in range(length))
    return password

def generate_password():
    length = int(entry_length.get())
    strength = strength_var.get()

    if strength == "Weak":
        password = generate_weak_password(length)
    elif strength == "Medium":
        password = generate_medium_password(length)
    elif strength == "Strong":
        password = generate_strong_password(length)

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def main():
    global entry_length, entry_password, strength_var

    root = tk.Tk()
    root.title("Random Password Generator")

    label_length = tk.Label(root, text="Enter the desired length of the password:")
    label_length.pack()

    entry_length = tk.Entry(root)
    entry_length.pack()

    label_strength = tk.Label(root, text="Select the strength of the password:")
    label_strength.pack()

    strength_var = tk.StringVar()
    strength_var.set("Weak")

    radio_weak = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak")
    radio_weak.pack()

    radio_medium = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium")
    radio_medium.pack()

    radio_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")
    radio_strong.pack()

    entry_password = tk.Entry(root)
    entry_password.pack()

    button_generate = tk.Button(root, text="Generate Password", command=generate_password)
    button_generate.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
