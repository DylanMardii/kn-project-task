import tkinter as tk # For creating the GUI
from tkinter import messagebox # For showing error messages in case of invalid input

def calculate_discount(original_price, discount_percentage):
    try:
        original_price = float(original_price)
        discount_percentage = float(discount_percentage)

        if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Please enter valid positive numbers for price and percentage (0-100).")

        discount_amount = (original_price * discount_percentage) / 100
        final_price = original_price - discount_amount

        return discount_amount, final_price
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        return None


def on_calculate(self):
    try:
        original_price_str = input_original_price.get().strip()
        quantity_str = input_quantity.get().strip()
        discount_percentage_str = input_discount_percentage.get().strip()

        if not original_price_str or not quantity_str or not discount_percentage_str:
            raise ValueError("All fields must be filled in.")

        original_price = float(original_price_str)
        quantity = int(quantity_str)
        discount_percentage = float(discount_percentage_str)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        return

    result = calculate_discount(quantity * original_price, discount_percentage)
    if result is not None:
        discount_amount, final_price = result
        label_result.config(text=f"Discount Amount: ${discount_amount:,.2f}\nFinal Price: ${final_price:,.2f}")
    

# Main application window
root = tk.Tk()
root.title("Discount Calculator")
# Set a fixed size for the window, remove this if you want it to be resized according to content
root.geometry("300x250") 

# Place widgets
label_original_price = tk.Label(root, text="Original Price:")
label_original_price.grid(row=0, column=0, padx=10, pady=10)

input_original_price = tk.Entry(root)
input_original_price.grid(row=0, column=1, padx=10, pady=10)

label_quantity = tk.Label(root, text="Quantity:")
label_quantity.grid(row=1, column=0, padx=10, pady=10)

input_quantity = tk.Entry(root)
input_quantity.grid(row=1, column=1, padx=10, pady=10)

label_discount_percentage = tk.Label(root, text="Discount Percentage:")
label_discount_percentage.grid(row=2, column=0, padx=10, pady=10)

input_discount_percentage = tk.Entry(root)
input_discount_percentage.bind("<Return>", on_calculate) # When pressing Enter to trigger calculation
input_discount_percentage.grid(row=2, column=1, padx=10, pady=10)

btn_submit = tk.Button(root, text="Calculate", command=on_calculate)
btn_submit.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()