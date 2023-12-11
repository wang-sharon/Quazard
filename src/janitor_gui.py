"""
This is the module to handle the GUI tab for Janitor
"""
import tkinter as tk
import tkinter.ttk as ttk
import janitor
import pandas as pd
from tkinter import messagebox
def create_janitor_tab(tab_control, dataframe=None):
    """    
    Parameters:
    - tab_control: The upper layer control from the main GUI
    - dataframe: The dataframe passed from previous component
    """
    janitor_tab = ttk.Frame(tab_control)
    tab_control.add(janitor_tab, text='Janitor')
    
    # Test dataframe
    if not dataframe: 
        df = pd.read_csv("../test/data/vt3 data cleaned not converted or aggregated.csv")
        columns = df.columns.tolist()
    
    # Create labels
    label1 = ttk.Label(janitor_tab, text="Select columns to be dropped:")
    label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    
    # Create a dropmenu with options of dataframe columns
    selected_values = []
    combobox = ttk.Combobox(janitor_tab, values=columns)
    combobox.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)
    
    # Create a box to display selected columns
    listbox = tk.Listbox(janitor_tab)
    listbox.grid(row=2, column=0, padx=30, pady=10, sticky=tk.W)
    
    # # Create a button to add selected values
    add_button1 = ttk.Button(janitor_tab, text="Add",
                             command=lambda: add_to_list(combobox, selected_values, listbox))
    add_button1.grid(row=3, column=0, padx=60, pady=5, sticky=tk.W)
    
    # Create a button to submit selected values
    drop_button = ttk.Button(janitor_tab, text="Drop Selected Columns",
                             command=lambda: drop_selected_columns(selected_values, df))
    drop_button.grid(row=1, column=1, padx=10, pady=10)
    
    # Create a button to clear selected columns
    clear_button = ttk.Button(janitor_tab, text="Clear List", command=lambda: clear_list(listbox))
    clear_button.grid(row=2, column=1, padx=10, pady=10)
    
def add_to_list(combobox, selected_values, listbox):
    """
    Parameters:
    - combobox: The comobbox widget
    - selected_values: The selected values from dropdown menu 
    - listbox: The display box 
    """
    selected_value = combobox.get()
    if selected_value not in selected_values:
        selected_values.append(selected_value)
        update_listbox(selected_values, listbox)

def update_listbox(selected_values, listbox):
    """
    Parameters:
    - selected_values: The selected values from dropdown menu 
    - listbox: The display box 
    """
    listbox.delete(0, tk.END)
    for value in selected_values:
        listbox.insert(tk.END, value)
        
def clear_list(listbox):
    """
    Parameters:
    - listbox: The display box for columns to be dropped
    """
    listbox.delete(0, tk.END)
    
def drop_selected_columns(selected_values, dataframe):
    """
    Parameters:
    - listbox: The display box for columns to be dropped
    
    Returns:
    - new_dataframe: The new dataframe without selected columns
    """
    if selected_values:
        try:
            new_dataframe = janitor.drop_cols(dataframe, selected_values)
            messagebox.showinfo("Columns Dropped", "Selected columns have been dropped.")
            return new_dataframe
        except ValueError:
            messagebox.showwarning("Dropping Failed", "Selected columns have not beed dropped properly!")
    else:
        messagebox.showwarning("Dropping Failed", "Invalid input!")