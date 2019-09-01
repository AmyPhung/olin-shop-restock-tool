import tkinter as tk
import pandas as pd
import numpy as np
import csv

class Page(tk.Frame):
    def __init__(self, page_num, inventory):
        tk.Frame.__init__(self)
        self.df = inventory[inventory["Drawer"] == page_num]
        print("here12")
        print(self.df)
        idx_list = np.where(inventory["Drawer"] == page_num)
        self.selection = []
        for idx in idx_list[0]:
            self.selection.append(createCheckbox(self, inventory["Name"][idx]))

    def show(self):
        self.lift()

    def updateSelections(self):
        checkboxes = []
        for s in self.selection:
            checkboxes.append(s.get())
        return checkboxes

    def getSelections(self):
        part_numbers = []

        checkboxes = self.updateSelections()
        self.df['Selected'] = checkboxes

        selected = self.df[self.df["Selected"] == 1]

        part_numbers = selected["Part Number"]
        return part_numbers

def createCheckbox(frame, item):
    var = tk.IntVar()
    tk.Checkbutton(frame, text=item, variable=var).pack(side="top", fill="both", expand=True)
    return var

class MainView(tk.Frame):
    def __init__(self, root, inventory):
        tk.Frame.__init__(self, root)
        self.pages = [Page(1, inventory),
                      Page(2, inventory)]

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        for page_idx in range(0,len(self.pages)):
            page = self.pages[page_idx]
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            tk.Button(buttonframe, text="Page " + str(page_idx + 1), command=page.lift).pack(side="left")

        create_btn = tk.Button(buttonframe, text="Create Order", command=self.createCSV)
        create_btn.pack(side="right")

        self.pages[0].show() # show first page

    def createCSV(self):
        part_numbers = []
        for page in self.pages:
            d = list(page.getSelections()) ##### FIX HERE
            part_numbers = part_numbers + d

        quantity = np.ones(len(part_numbers))

        data = {'Part Numbers': part_numbers,
                'Quantity': quantity
        }

        df = pd.DataFrame(data, columns= ['Part Numbers','Quantity'])
        df.to_csv('order.csv', index = None, header=True)

if __name__ == "__main__":
    inventory = pd.read_csv('master_inventory.csv')

    root = tk.Tk()
    main = MainView(root, inventory)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x1000")


    # root.mainloop()
    while True:
        root.update()
