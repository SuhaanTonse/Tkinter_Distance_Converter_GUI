import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

feet_value = tk.StringVar()
metres_value = tk.StringVar()

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

main = ttk.Frame(root,padding=(60,30))
main.grid()

root.columnconfigure(0,weight=1)

metres_label = ttk.Label(main,text="Metres")
metres_input = ttk.Entry(main,textvariable=metres_value,width=10,font=(None,15))
feet_label = ttk.Label(main,text="Feet")
feet_display = ttk.Label(main,textvariable=feet_value)
calc_button = ttk.Button(main,text="Calculate", command=calculate_feet)

metres_label.grid(row=0,column=0, sticky='W')
metres_input.grid(row=0,column=1,sticky='EW')
metres_input.focus()

feet_label.grid(row=1,column=0,sticky='W')
feet_display.grid(row=1,column=1,sticky='EW')

calc_button.grid(row=2,column=0,columnspan=2,sticky='EW')

for child in main.winfo_children():
    child.grid_configure(padx=15,pady=15)

root.bind("<Return>",calculate_feet)
root.bind("<KP_Enter>",calculate_feet)

root.mainloop()

