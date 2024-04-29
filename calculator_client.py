import tkinter as tk
import requests


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        response = requests.post('http://127.0.0.1:5000/calculate',
                                 json={'num1': num1, 'num2': num2, 'operator': operator})
        data = response.json()

        if 'error' in data:
            result_label.config(text="Error: " + data['error'])
        else:
            result_label.config(text="Result: " + str(data['result']))
    except ValueError:
        result_label.config(text="Error: Invalid input!")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields for numbers
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Create dropdown menu for operator selection
operator_var = tk.StringVar(root)
operator_var.set('+')  # default operator
operator_dropdown = tk.OptionMenu(root, operator_var, '+', '-', '*', '/')
operator_dropdown.grid(row=0, column=2, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, columnspan=3, padx=5, pady=5)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=3, padx=5, pady=5)

root.mainloop()
