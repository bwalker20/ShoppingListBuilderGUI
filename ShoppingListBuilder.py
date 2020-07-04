import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Recipe
class App(tk.Frame):
    def __init__(self, master=None):
        self.recipe_list = Recipe.Recipe()
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.geometry('400x400')
        self.create_widgets()

    def create_widgets(self):
        self.add_new_recipe = tk.Button(self.master, text = 'Add New Recipe', command=self.add_new)
        self.add_new_recipe.pack()
        self.recipe_cb = ttk.Combobox(self.master, values = self.recipe_list.get_recipes())
        self.recipe_cb.pack()
        self.recipe_sel = tk.Button(self.master, text = 'Select Recipe', command= lambda: self.select_recipe(self.recipe_cb.get()))
        self.recipe_sel.pack()
        self.exit = tk.Button(self.master, text = 'Exit', fg = 'red', command = self.master.destroy)
        self.exit.pack()

    def add_new(self):
        add_new_window = tk.Toplevel(self.master)
        add_new_window.title("Add New Recipe Menu")
        add_new_window.geometry("200x200")
        name_label = tk.Label(add_new_window, text = 'Recipe Name:')
        name_label.pack()
        name_text = tk.Entry(add_new_window, width=10)
        name_text.pack()
        amount_label = tk.Label(add_new_window, text = 'Number of ingredients:')
        amount_label.pack()
        amount_text = tk.Entry(add_new_window, width = 4)
        amount_text.pack()
        ingredient_btn = tk.Button(add_new_window, text = 'Submit', command = lambda: self.add_new_ingredients(name_text.get(), amount_text.get(), add_new_window))
        ingredient_btn.pack()

    def add_new_ingredients(self, name, amount, window):
        window.destroy()
        if self.recipe_list.select_recipe(name, None) == True:
            messagebox.showerror(title = 'Error', message = 'This Recipe already exists, please enter a different name')
        else:
            add_new_window = tk.Toplevel(self.master)
            add_new_window.title("Build Recipe Menu")
            #add_new_window.geometry('600x600')
            entry_list_names_l = []
            entry_list_names = []
            entry_list_amounts_l = []
            entry_list_amounts = []
            for i in range(int(amount)):
                entry_list_names.append(tk.Entry(add_new_window))
                entry_list_amounts.append(tk.Entry(add_new_window))
                entry_list_names_l.append(tk.Label(add_new_window, text = 'Name of ingredient:'))
                entry_list_amounts_l.append(tk.Label(add_new_window, text = 'Amount of ingredient:'))
                entry_list_names_l[i].grid(row = i, column = 0)
                entry_list_names[i].grid(row = i, column = 1)
                entry_list_amounts_l[i].grid(row = i, column = 2)
                entry_list_amounts[i].grid(row = i, column = 3)
            create_list_btn = tk.Button(add_new_window, text = 'Submit', command = lambda: self.create_list(name, add_new_window, amount, entry_list_names, entry_list_amounts))
            create_list_btn.grid(row = int(amount), column = 3)
        
    def create_list(self, name, window, amount, entry_list_names, entry_list_amounts):
        ing_list = []
        for i in range(int(amount)):
            ing_list.append(tuple((entry_list_names[i].get(), entry_list_amounts[i].get())))
        self.recipe_list.add_new(name, ing_list)
        window.destroy()

    def select_recipe(self, name):
        print(name)
        print("Finish This")


        


root = tk.Tk()
app = App(master=root)
app.mainloop()