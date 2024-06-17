import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import sys
import csv
import config_gui


class EditableTableApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Editable Table")

        self.data = []

        # Configure the Treeview style
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30, background="black", foreground="white", fieldbackground="black")
        self.style.configure("Treeview.Heading", font=("Arial", 16, "bold"), background="black", foreground="white")

        # Apply a custom layout to the Treeview headings to set the background color
        self.style.map("Treeview.Heading",
                       background=[('active', 'black'), ('!active', 'black')],
                       foreground=[('active', 'white'), ('!active', 'white')])

        self.tree = ttk.Treeview(root, columns=('Name', 'Gender'), show='headings', style="Treeview")
        self.tree.heading('Name', text='Name')
        self.tree.heading('Gender', text='Gender')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree["displaycolumns"] = ("Name", "Gender")
        self.tree["show"] = ("headings", "tree")

        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.bind('<Delete>', self.del_button)
        self.tree.bind('<BackSpace>', self.del_button)

        self.populate_table()

        self.add_button = ctk.CTkButton(root, text="Add Row", command=self.add_row, font=("Arial", 16),
                                        fg_color="black", text_color="white")
        self.done_button = ctk.CTkButton(root, text="Done", command=self.export_namen, font=("Arial", 16),
                                         fg_color="black", text_color="white")

        self.add_button.pack(pady=10)

        self.done_button.pack(pady=10)

    def export_namen(self):
        with open("namen.csv", "w") as file:
            for i in self.tree.get_children():
                print(self.tree.item(i)['values'])
                file.write(f"{self.tree.item(i)['values'][0]}, {self.tree.item(i)['values'][1]}\n")
        self.root.destroy()
        config_gui.main()



    def populate_table(self):
        try:
            with open("namen.csv", 'r') as file:
                self.data = []
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    self.data.append(line)

        except Exception as e:
            print(e)
            self.data = [
                ('Alice', 'meisje'),
                ('Bob', 'jongen'),
                ('Charlie', 'jongen'),
                ('David', 'jongen'),
                ('Eve', 'meisje')
            ]
        for row in self.data:
            self.tree.insert('', tk.END, values=row)

    def on_double_click(self, event):
        item = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        if item and column:
            self.edit_cell(item, column)

    def del_button(self, event):
        try:
            item = self.tree.identify_row(event.y)
            person = self.tree.item(item)['values']
            #  self.data.remove(person)
            self.tree.pack()
            self.tree.delete(item)
        except Exception as e:
            print(e)

    def edit_cell(self, item, column):
        col_index = int(column[1:]) - 1
        old_value = self.tree.item(item, 'values')[col_index]
        entry_popup = EditPopup(self.root, old_value, self.update_cell, item, col_index)
        self.root.wait_window(entry_popup.top)

    def update_cell(self, new_value, item, col_index):
        current_values = list(self.tree.item(item, 'values'))
        current_values[col_index] = new_value
        self.tree.item(item, values=current_values)

    def add_row(self):
        new_row_popup = AddRowPopup(self.root, self.insert_row)
        self.root.wait_window(new_row_popup.top)

    def insert_row(self, values):
        self.tree.insert('', tk.END, values=values)


class EditPopup:
    def __init__(self, parent, old_value, callback, item, col_index):
        self.top = tk.Toplevel(parent)
        self.top.title("Edit Cell")

        self.callback = callback
        self.item = item
        self.col_index = col_index
        tk.Label(self.top, text="New Value:", font=("Arial", 14), background="black", foreground="white").pack(pady=5)
        self.entry = ctk.CTkEntry(self.top, font=("Arial", 14), fg_color="black", text_color="white")
        self.entry.pack(pady=5)
        self.entry.insert(0, old_value)
        self.entry.focus_set()

        tk.Button(self.top, text="Save", command=self.save, font=("Arial", 14), bg="black", fg="white").pack(pady=5)

    def save(self):
        new_value = self.entry.get()
        self.callback(new_value, self.item, self.col_index)
        self.top.destroy()



class AddRowPopup:
    def __init__(self, parent, callback):
        self.top = tk.Toplevel(parent)
        self.top.title("Add New Row")

        self.callback = callback

        self.entries = []
        labels = ['Name', 'Gender']
        for label in labels:
            tk.Label(self.top, text=f"{label}:", font=("Arial", 14), background="white", foreground="black").pack(
                pady=5)
            entry = ctk.CTkEntry(self.top, font=("Arial", 14), fg_color="black", text_color="white")
            entry.pack(pady=5)
            self.entries.append(entry)

        tk.Button(self.top, text="Add", command=self.add, font=("Arial", 14), bg="black", fg="white").pack(pady=10)

    def add(self):
        values = [entry.get() for entry in self.entries]
        self.callback(values)
        self.top.destroy()


ctk.set_appearance_mode("dark")  # Modes: "system" (default), "light", "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
root = ctk.CTk()
root.geometry("600x400")
app = EditableTableApp(root)

root.mainloop()
