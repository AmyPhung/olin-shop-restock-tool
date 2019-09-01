import tkinter as tk
import pandas as pd
import numpy as np
import csv

class Page(tk.Frame):
    def __init__(self, page_num, inventory):
        tk.Frame.__init__(self)

        self.df = inventory[inventory["Drawer"] == page_num]

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(self, selectmode="multiple")
        self.listbox.pack(fill="both", expand=True)

        idx_list = np.where(inventory["Drawer"] == page_num)
        for idx in idx_list[0]:
            self.listbox.insert(tk.END, inventory["Name"][idx])

        # attach listbox to scrollbar
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.part_numbers = []

    def show(self):
        self.lift()

    def updatePartNumbers(self):
        values = [self.listbox.get(idx) for idx in self.listbox.curselection()]

        selected = self.df[self.df["Name"].isin(values)] #todo: make this not a copy

        self.part_numbers = selected["McMaster #"]

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
            tk.Button(buttonframe, text="Page " + str(page_idx + 1), command=lambda: self.updateFrame(page_idx)).pack(side="left")

        create_btn = tk.Button(buttonframe, text="Create Order", command=self.createCSV)
        create_btn.pack(side="right")

        self.current_frame = 0
        self.updateFrame(0)

    def updateFrame(self, page_idx):
        self.pages[self.current_frame].updatePartNumbers() # update old page
        self.pages[page_idx].show() # show new page
        self.current_frame = page_idx

    def createCSV(self):
        self.updateFrame(self.current_frame)
        part_numbers = []
        for page in self.pages:
            d = list(page.part_numbers)
            part_numbers = part_numbers + d

        quantity = np.ones(len(part_numbers))

        data = {'Part Numbers': part_numbers,
                'Quantity': quantity
        }

        df = pd.DataFrame(data, columns= ['Part Numbers','Quantity'])
        df.to_csv('order.csv', index = None, header=True)

        print("Saved to file!")

if __name__ == "__main__":
    inventory = pd.read_csv('master_inventory.csv')

    root = tk.Tk()
    main = MainView(root, inventory)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x1000")


    root.mainloop()
    # while True:
    #     root.update()
