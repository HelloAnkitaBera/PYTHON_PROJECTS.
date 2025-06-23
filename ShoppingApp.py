import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Shopping Cart")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f8ff")  

       
        header = tk.Label(root, text="🛍️ Welcome to Ankita's Store", font=("Helvetica", 16, "bold"), bg="#4682B4", fg="white", pady=10)
        header.pack(fill="x")

        self.products = [
            Product(1, "Laptop", 120000.00),
            Product(2, "Smartphone", 50000.00),
            Product(3, "Headphones", 1500.00),
            Product(4, "Keyboard", 500.00),
        ]

        self.cart = []

        # Product display area
        product_frame = tk.LabelFrame(root, text="📦 Available Products", bg="#f0f8ff", fg="#333", font=("Arial", 12, "bold"), padx=10, pady=10, bd=3, relief="groove")
        product_frame.pack(pady=10)

        for product in self.products:
            self.display_product(product, product_frame)

        # Cart output
        self.cart_display = tk.Text(root, height=10, width=70, bd=3, relief="sunken", bg="#fffaf0")
        self.cart_display.pack(pady=10)

        # Cart Buttons
        btn_frame = tk.Frame(root, bg="#f0f8ff")
        btn_frame.pack()
        tk.Button(btn_frame, text="🛒 View Cart", command=self.view_cart, bg="#90EE90", fg="black", padx=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💳 Checkout Cart", command=self.checkout_cart, bg="#FFD700", fg="black", padx=10).grid(row=0, column=1, padx=10)

    def display_product(self, product, container):
        frame = tk.Frame(container, bg="#e6f2ff", bd=2, relief="ridge", padx=5, pady=5)
        frame.pack(fill="x", pady=5)

        label = tk.Label(frame, text=f"{product.id}. {product.name} - ₹{product.price:.2f}", bg="#e6f2ff", font=("Arial", 11))
        label.pack(side="left")

        quantity_entry = tk.Entry(frame, width=4)
        quantity_entry.insert(0, "1")
        quantity_entry.pack(side="left", padx=5)

        tk.Button(frame, text="Add to Cart", command=lambda p=product, q=quantity_entry: self.add_to_cart(p, q), bg="#add8e6", padx=5).pack(side="left", padx=5)
        tk.Button(frame, text="Buy Now", command=lambda p=product, q=quantity_entry: self.buy_now(p, q), bg="#ffb6c1", padx=5).pack(side="left", padx=5)

    def add_to_cart(self, product, quantity_entry):
        try:
            quantity = int(quantity_entry.get())
            self.cart.append((product, quantity))
            messagebox.showinfo("Added", f"✅ Added {quantity} x {product.name} to cart.")
        except ValueError:
            messagebox.showerror("Error", "❌ Enter a valid quantity.")

    def view_cart(self):
        if not self.cart:
            self.cart_display.delete(1.0, tk.END)
            self.cart_display.insert(tk.END, "🛒 Your cart is empty.\n")
            return

        self.cart_display.delete(1.0, tk.END)
        total = 0
        self.cart_display.insert(tk.END, "\n🧾 Cart Contents:\n\n")
        for product, quantity in self.cart:
            subtotal = product.price * quantity
            self.cart_display.insert(tk.END, f"{product.name} x {quantity} = ₹{subtotal:.2f}\n")
            total += subtotal
        self.cart_display.insert(tk.END, f"\nTotal: ₹{total:.2f}")

    def checkout_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart Empty", "🛒 Your cart is empty.")
            return

        self.view_cart()
        self.cart_display.insert(tk.END, "\n\n💳 Checkout complete. (Simulated payment)")
        self.cart.clear()

    def buy_now(self, product, quantity_entry):
        try:
            quantity = int(quantity_entry.get())
            total = product.price * quantity
            self.cart_display.delete(1.0, tk.END)
            self.cart_display.insert(tk.END, f"🛒 Buying {quantity} x {product.name}\nTotal: ₹{total:.2f}")
            self.cart_display.insert(tk.END, "\n\n💳 Payment complete. (Simulated)")
        except ValueError:
            messagebox.showerror("Error", "❌ Enter a valid quantity.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
