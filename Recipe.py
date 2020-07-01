import os
from pathlib import Path
from os import path

class Recipe:
    def __init__(self):
        self.cur_list = []
        doc_path = os.path.expanduser("~/Documents")
        if path.exists(doc_path + '/Recipes') == False:
            file_path = doc_path + '/Recipes'
            access = 0o777
            try:
                os.mkdir(file_path, access)
                print("Recipes Folder has been created in Documents")
            except OSError:
                print("cannot create valid directory for recipes, try running program as admin")

    def add_new(self):
        print("Enter in the name of the recipe")
        name = input()
        while path.exists(doc_path + '/Recipes/{}.txt'.format(name)) == True:
            print("This recipe name already exists, please try a different name")
            name = input()
        print("Enter in the number of different ingredients that are in the recipe")
        while True:
            try:
                num_ingrediants = int(input())
            except ValueError:
                print("Not a valid number of ingredients, please try again")
            else:
                break
        ingrediant_list = []
        for i in range(int(num_ingrediants)):
            print("Enter the name of ingredient {} and the units (Lbs, oz, etc.) *Amount needed will follow*".format(i+1))
            ingrediant_name = input()
            print("Enter the amount needed")
            ingrediant_amount = input()
            ingrediant_list.append(tuple((ingrediant_name, ingrediant_amount)))
        with open(doc_path + '/Recipes/{}.txt'.format(name), "w") as fp:
            fp.write('\n'.join('%s,%s' % x for x in ingrediant_list))

    def select(self, shopping_list):
        f = []
        for (dirpath, dirnames, filenames) in os.walk('./Recipes'):
            f.extend(filenames)
            break
        print("Current Recipies to Choose from:")
        for i in f:
            print(Path(i).with_suffix(''))
        print("Enter what recipe you want to add, enter 'None' if you want to return to the main menu")
        name = input()
        if name == 'None':
            return
        if path.exists(doc_path + '/Recipes/{}.txt'.format(name)) == False:
            print("This is not a valid recipe")
            return
        with open(doc_path + '/Recipes/{}.txt'.format(name), "r") as fp:
            for i in fp.readlines():
                tmp = i.split(",")
                if tmp[0] in shopping_list:
                    shopping_list[tmp[0]] = shopping_list[tmp[0]] + float(tmp[1])
                else:
                    shopping_list[tmp[0]] = float(tmp[1])
