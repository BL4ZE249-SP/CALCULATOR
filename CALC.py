
#!/usr/bin/python3
import tkinter as tk

root = tk.Tk()

root.geometry("300x400")
btn_color="green"
lbl_text="Tom's Calculator"

############################################################################################


top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, columnspan=4)
 
title_label = tk.Label(top_frame, text=lbl_text, font=("Arial", 16), bg="lightgray")
title_label.grid(row=0, column=0, columnspan=4, sticky="we")
entry = tk.Entry(top_frame, font=("Arial", 18), bd=5, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=1, column=0, columnspan=4, pady=10)
 
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

 
