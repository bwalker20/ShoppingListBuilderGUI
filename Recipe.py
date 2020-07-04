import os
from pathlib import Path
from os import path

class Recipe:
    def __init__(self):
        self.cur_list = []
        self.doc_path = os.path.expanduser("~/Documents")
        if path.exists(self.doc_path + '/Recipes') == False:
            file_path = self.doc_path + '/Recipes'
            access = 0o777
            try:
                os.mkdir(file_path, access)
                print("Recipes Folder has been created in Documents")
            except OSError:
                print("cannot create valid directory for recipes, try running program as admin")


    def add_new(self, name, ingredients):
        #print("Adds a new recipe to the recipes folder")
        if len(ingredients) == 0:
            return
        with open(self.doc_path + '/Recipes/{}.txt'.format(name), 'w') as fp:
            fp.write('\n'.join('%s,%s' % x for x in ingredients))

    def get_recipes(self):
        #print("Returns a list of all the recipes")
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.doc_path + '/Recipes'):
            f.extend(filenames)
            break
        for i in range(len(f)):
            f[i] = Path(f[i]).with_suffix('')
        return f

    def select_recipe(self, name, shopping_list):
        #print("Adds all the ingredients of specified recipe to the shopping list disctionary, return true if recipe exists and false if recipe doesn't")
        if shopping_list == None:
            return path.exists(self.doc_path + '/Recipes/{}.txt'.format(name))
        with open(self.doc_path + '/Recipes/{}.txt'.format(name), "r") as fp:
            for i in fp.readlines():
                tmp = i.split(",")
                if tmp[0] in shopping_list:
                    shopping_list[tmp[0]] = shopping_list[tmp[0]] + float(tmp[1])
                else:
                    shopping_list[tmp[0]] = float(tmp[1])
