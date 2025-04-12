import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random

# File for saving contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Funky Colors
COLORS = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFD700"]

# Add a new contact with animation
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        update_contact_list()
        
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        funky_label.config(text=f"🎉 {name} Added!", fg=random.choice(COLORS))
        root.after(1500, lambda: funky_label.config(text=""))  # Remove text after 1.5s
    else:
        messagebox.showwarning("Oops!", "All fields are required!")

# Update contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, f" {name}")

# View contact details
def view_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0])[2:]  # Remove emoji prefix
        info = contacts[name]
        messagebox.showinfo("👀 Contact Info", f"📛 Name: {name}\n📞 Phone: {info['phone']}\n📧 Email: {info['email']}")
    else:
        messagebox.showwarning("Oops!", "No contact selected!")

# Edit contact
def edit_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0])[2:]
        new_phone = simpledialog.askstring("Edit Contact", f"New phone for {name}?", initialvalue=contacts[name]["phone"])
        new_email = simpledialog.askstring("Edit Contact", f"New email for {name}?", initialvalue=contacts[name]["email"])

        if new_phone and new_email:
            contacts[name] = {"phone": new_phone, "email": new_email}
            save_contacts()
            messagebox.showinfo("Updated!", f"{name} is now updated! 🎯")
    else:
        messagebox.showwarning("Oops!", "No contact selected!")

# Delete contact
def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0])[2:]
        confirm = messagebox.askyesno("⚠ Delete Contact", f"Are you sure you want to remove {name}?")
        if confirm:
            del contacts[name]
            save_contacts()
            update_contact_list()
            messagebox.showinfo("Deleted!", f"{name} is gone! 💨")
    else:
        messagebox.showwarning("Oops!", "No contact selected!")

# GUI Setup
root = tk.Tk()
root.title("📞 Funky Contact Manager 🎶")
root.geometry("420x520")
root.configure(bg="#121212")  # Dark Theme

contacts = load_contacts()

# Funky Label
funky_label = tk.Label(root, text="", font=("Comic Sans MS", 14, "bold"), bg="#121212")
funky_label.pack()

# Input Fields
tk.Label(root, text="📛 Name:", font=("Comic Sans MS", 12, "bold"), bg="#121212", fg="white").pack()
name_entry = tk.Entry(root, font=("Comic Sans MS", 12), bg="#333333", fg="white")
name_entry.pack()

tk.Label(root, text="📞 Phone:", font=("Comic Sans MS", 12, "bold"), bg="#121212", fg="white").pack()
phone_entry = tk.Entry(root, font=("Comic Sans MS", 12), bg="#333333", fg="white")
phone_entry.pack()

tk.Label(root, text="📧 Email:", font=("Comic Sans MS", 12, "bold"), bg="#121212", fg="white").pack()
email_entry = tk.Entry(root, font=("Comic Sans MS", 12), bg="#333333", fg="white")
email_entry.pack()

# Buttons
tk.Button(root, text="✨ Add Contact", command=add_contact, bg="#FF5733", fg="white", font=("Comic Sans MS", 12, "bold")).pack(pady=5)

# Contact List
contact_listbox = tk.Listbox(root, font=("Comic Sans MS", 12), bg="#333333", fg="white")
contact_listbox.pack(fill=tk.BOTH, expand=True)
update_contact_list()

# Action Buttons
tk.Button(root, text="👀 View", command=view_contact, bg="#33FF57", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
tk.Button(root, text="✏ Edit", command=edit_contact, bg="#FFD700", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
tk.Button(root, text="🗑 Delete", command=delete_contact, bg="red", fg="white", font=("Comic Sans MS", 12, "bold")).pack(pady=5)

# Run App
root.mainloop()
