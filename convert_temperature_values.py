import tkinter as tk
from cProfile import label
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        if var.get() == "Celsius to Fahrenheit":
            converted_temp = (temp * 9/5) + 32
            label_result.config(text=f"{temp}C = {converted_temp:.2f}F")
        else:
            converted_temp =(temp -32) * 5/9
            label_result.config(text=f"{temp}F = {converted_temp:.2f}C")
    except ValueError:
        messagebox.showerror("Invalid input","please enter valid input")

root = tk.Tk()
root.title("Temperature Converter")

label_instruction = tk.Label(root, text="Enter the temperature:")
label_instruction.grid(row=0, column=0, padx=10, pady=10)

entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

var = tk.StringVar(value="Celsius to Fahrenheit")
dropdown = tk.OptionMenu(root, var, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()