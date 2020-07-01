import tkinter as tk
import Recipe
class App(tk.Frame):
    def __init__(self, master=None):
        recipe_list = Recipe.__init__()
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.geometry('200x200')
        self.create_widgets()

    def create_widgets(self):
        self.add_new_recipe = tk.Button(self, text = 'Add New Recipe')#, command=Recipe.add_new())
        self.add_new_recipe.pack(side = 'top')
        self.exit = tk.Button(self, text = 'Exit', fg = 'red', command = self.master.destroy)
        self.exit.pack(side='bottom')

root = tk.Tk()
app = App(master=root)
app.mainloop()