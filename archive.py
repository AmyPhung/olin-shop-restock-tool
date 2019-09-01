import tkinter as tk
import pandas as pd
import numpy as np


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.index_list = None
    def setData(self, data):
        self.data = data
    def setContents(self, index_list):
        self.index_list = contents
    def show(self):
        self.lift()

def createCheckbox(frame, item):
    var = tk.IntVar()
    tk.Checkbutton(frame, text=item, variable=var).pack(side="top", fill="both", expand=True)
    return var

# For drawer 1 contents
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

       self.selection = []

       for idx in self.index_list:
           self.selection.append(createCheckbox(self, ))

# For drawer 2 contents
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

#
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.p1 = Page1(self)
        self.p2 = Page2(self)
        self.p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=self.p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=self.p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=self.p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        self.p1.show()

if __name__ == "__main__":
    inventory = pd.read_csv('master_inventory.csv')

    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")

    main.p1.setContents(np.where(inventory["Drawer"] == 1))
    main.p2.setContents(np.where(inventory["Drawer"] == 2))
    main.p3.setContents(np.where(inventory["Drawer"] == 3))

    # root.mainloop()
    while True:
        root.update()
        # print(main.p1.var1.get())
        # print(inventory["Drawer"])
        # print(np.where(inventory["Drawer"] == 2))
