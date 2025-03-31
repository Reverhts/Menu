import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

def initialize_db():
    conn = sqlite3.connect("inventory1.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE,
                        perishable BOOLEAN,
                        qty INTEGER,
                        description TEXT)''')
    conn.commit()
    conn.close()

class InventoryAppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        
        self.label = tk.Label(root, text="Inventory Items", font=("Arial", 15))
        self.label.pack()

        self.listbox = tk.Listbox(root, width=55, height=13)
        self.listbox.pack()
        
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()
        
        self.edit_button = tk.Button(root, text="Edit Item", command=self.edit_item)
        self.edit_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()
        
        self.view_button = tk.Button(root, text="View Item", command=self.view_item)
        self.view_button.pack()
        
        self.load_inventory()
    
    def execute_query(self, query, params=()):
        conn = sqlite3.connect("inventory1.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def load_inventory(self):
        self.listbox.delete(0, tk.END)
        conn = sqlite3.connect("inventory1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM inventory")
        items = cursor.fetchall()
        conn.close()
        for item in items:
            self.listbox.insert(tk.END, item[0])

    def add_item(self):
        item_name = simpledialog.askstring("Input", "Enter item name:")
        if item_name:
            perishable = simpledialog.askstring("Input", "Is the item perishable? (yes/no):").strip().lower() == "yes"
            quantity = simpledialog.askinteger("Input", "Enter quantity:", minvalue=1)
            description = simpledialog.askstring("Input", "Enter item description:")
            if quantity is not None and description is not None:
                try:
                    self.execute_query("INSERT INTO inventory (name, perishable, qty, description) VALUES (?, ?, ?, ?)", (item_name, perishable, quantity, description))
                    self.load_inventory()
                except sqlite3.IntegrityError:
                    messagebox.showwarning("Warning", "Item already exists. Use edit option to update.")
    
    def edit_item(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No item selected!")
            return
        item_name = self.listbox.get(selected[0])
        new_quantity = simpledialog.askinteger("Input", f"Enter new quantity for {item_name}:", minvalue=1)
        new_description = simpledialog.askstring("Input", f"Enter new description for {item_name}:")
        if new_quantity is not None and new_description is not None:
            self.execute_query("UPDATE inventory SET qty = ?, description = ? WHERE name = ?", (new_quantity, new_description, item_name))
            self.load_inventory()
    
    def remove_item(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No item selected!")
            return
        item_name = self.listbox.get(selected[0])
        self.execute_query("DELETE FROM inventory WHERE name = ?", (item_name,))
        self.load_inventory()
    
    def view_item(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No item selected!")
            return
        item_name = self.listbox.get(selected[0])
        conn = sqlite3.connect("inventory1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT perishable, qty, description FROM inventory WHERE name = ?", (item_name,))
        details = cursor.fetchone()
        conn.close()
        if details:
            perishable_status = "Yes" if details[0] else "No"
            messagebox.showinfo("Item Details", f"Item: {item_name}\nPerishable: {perishable_status}\nQuantity: {details[1]}\nDescription: {details[2]}")

if __name__ == "__main__":
    initialize_db()
    root = tk.Tk()
    app_tk = InventoryAppTkinter(root)
    root.mainloop()