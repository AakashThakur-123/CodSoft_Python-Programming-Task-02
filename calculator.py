import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Label and Entry for the first number
        self.label_num1 = tk.Label(self.root, text="Enter first number:", font=('Arial', 14))
        self.label_num1.pack(pady=10)
        self.entry_num1 = tk.Entry(self.root, font=('Arial', 14))
        self.entry_num1.pack(pady=10)

        # Label and Entry for the second number
        self.label_num2 = tk.Label(self.root, text="Enter second number:", font=('Arial', 14))
        self.label_num2.pack(pady=10)
        self.entry_num2 = tk.Entry(self.root, font=('Arial', 14))
        self.entry_num2.pack(pady=10)

        # Label for operation selection
        self.label_operation = tk.Label(self.root, text="Choose an operation:", font=('Arial', 14))
        self.label_operation.pack(pady=10)

        # Frame for operation buttons
        self.operation_frame = tk.Frame(self.root)
        self.operation_frame.pack(pady=10)

        # Operation buttons
        self.add_button = tk.Button(self.operation_frame, text="+", font=('Arial', 14), width=5, command=lambda: self.calculate("add"))
        self.add_button.grid(row=0, column=0, padx=5)
        self.subtract_button = tk.Button(self.operation_frame, text="-", font=('Arial', 14), width=5, command=lambda: self.calculate("subtract"))
        self.subtract_button.grid(row=0, column=1, padx=5)
        self.multiply_button = tk.Button(self.operation_frame, text="*", font=('Arial', 14), width=5, command=lambda: self.calculate("multiply"))
        self.multiply_button.grid(row=0, column=2, padx=5)
        self.divide_button = tk.Button(self.operation_frame, text="/", font=('Arial', 14), width=5, command=lambda: self.calculate("divide"))
        self.divide_button.grid(row=0, column=3, padx=5)

        # Label for displaying the result
        self.label_result = tk.Label(self.root, text="Result:", font=('Arial', 14))
        self.label_result.pack(pady=10)

        # Result display
        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.result_label = tk.Label(self.root, textvariable=self.result_var, font=('Arial', 14), fg="blue")
        self.result_label.pack(pady=10)

    def calculate(self, operation):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
            self.result_var.set(f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
