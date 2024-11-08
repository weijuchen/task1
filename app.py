import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("GUI Ver1 @v0.02 2024-03-26")
root.geometry("800x400")


notebook = ttk.Notebook(root)


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="page 1")


button1 = tk.Button(
    tab1,
    text="按鈕 1",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 1 被點擊"),
)
button1.pack(pady=20)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="page2")


button2 = tk.Button(
    tab2,
    text="按鈕 2",
    font=("Arial", 16),
    command=lambda: print("Page 2 按鈕 2 被點擊"),
)
button2.pack(pady=20)


notebook.pack(expand=True, fill="both")


root.mainloop()
