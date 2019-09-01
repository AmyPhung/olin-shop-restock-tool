import tkinter as tk

root = tk.Tk()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, selectmode="multiple")
listbox.pack()

for i in range(100):
    listbox.insert(tk.END, i)

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def callback():
    values = [listbox.get(idx) for idx in listbox.curselection()]
    print(values)

b = tk.Button(root, text="OK", command=callback)
b.pack()


root.mainloop()
