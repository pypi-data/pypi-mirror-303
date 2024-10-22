import os
import tkinter as tk
from tkinter import simpledialog

class FolderSelectionDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initial_dir):
        self.initial_dir = initial_dir
        self.selected_folder = None
        super().__init__(parent, title=title)

    def body(self, master):
        self.geometry("400x300")
        self.folder_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=15)
        self.folder_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.populate_listbox(self.initial_dir)
        
        self.folder_listbox.bind("<Double-Button-1>", self.on_double_click)

        return self.folder_listbox

    def populate_listbox(self, folder):
        """Populates the listbox with folders."""
        self.folder_listbox.delete(0, tk.END)
        folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
        for folder_name in folders:
            self.folder_listbox.insert(tk.END, folder_name)
        self.selected_folder = folder

    def on_double_click(self, event):
        """Handles double-click event to move into a directory."""
        selection = self.folder_listbox.curselection()
        if selection:
            selected_folder = self.folder_listbox.get(selection[0])
            new_path = os.path.join(self.selected_folder, selected_folder)
            self.populate_listbox(new_path)

    def apply(self):
        """Set the selected folder path."""
        selection = self.folder_listbox.curselection()
        if selection:
            selected_folder_name = self.folder_listbox.get(selection[0])
            self.selected_folder = os.path.join(self.selected_folder, selected_folder_name)
        else:
            self.selected_folder = self.selected_folder
