import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

# GUI Setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("854x650")
root.config(bg="#f2f2f2")

header = tk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold"), bg="#4682B4", fg="white", pady=10)
header.pack(fill="x")



def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def view_contacts():
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c['name'].lower() or query in c['phone']:
            contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def delete_contact():
    try:
        selected = contact_list.curselection()[0]
        contacts.pop(selected)
        messagebox.showinfo("Deleted", "Contact deleted successfully.")
        view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")

def update_contact():
    try:
        index = contact_list.curselection()[0]
        contact = contacts[index]
        name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact["name"])
        phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact["phone"])
        email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact["email"])
        address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact["address"])

        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            messagebox.showinfo("Updated", "Contact updated successfully!")
            view_contacts()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a contact to update.")



tk.Label(root, text="Contact Name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone Number:").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

tk.Label(root, text="Company:").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white").pack(pady=5)

tk.Label(root, text="Search Contact:").pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()
tk.Button(root, text="Search", background="violet", fg="white", command=search_contact).pack(pady=5)

contact_list = tk.Listbox(root, width=60)
contact_list.pack(pady=10)

tk.Button(root, text="View All Contacts",bg="orange", fg="white", command=view_contacts).pack()
tk.Button(root, text="Update Selected", command=update_contact, bg="#2196F3", fg="white").pack(pady=2)
tk.Button(root, text="Delete Selected", command=delete_contact, bg="#f44336", fg="white").pack(pady=2)

root.mainloop()
