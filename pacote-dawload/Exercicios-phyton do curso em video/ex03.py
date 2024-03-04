import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")

        self.entry = ttk.Entry(self.root, font=("Helvetica", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sqrt", 1, 4), ("sin", 2, 4), ("cos", 3, 4), ("tan", 4, 4),
            ("(", 1, 5), (")", 2, 5), ("^", 3, 5), ("C", 4, 5)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i-1, weight=1)

    def button_click(self, value):
        current_text = self.entry.get()

        if value == "=":
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif value == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

