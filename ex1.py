import tkinter as tk
from tkinter import *

step = 50


root = Tk()
root.title("BRUH CONTROL.COM")
root.geometry("700x700")



lmao = Label(root, text="SIUUUU")
lmao.place(x = 300, y = 300)


fbutt = Button(text="^", command = lambda : (lmao.place(x = lmao.winfo_x(), y = lmao.winfo_y() - step)))
fbutt.pack()
fbutt.place(x = 350, y = 620)

rbutt = tk.Button(text=">", command = lambda : (lmao.place(x = lmao.winfo_x() + step, y = lmao.winfo_y())))
rbutt.pack()
rbutt.place(x = 400, y = 650)

bbutt = tk.Button(text="v", command = lambda : (lmao.place(x = lmao.winfo_x(), y = lmao.winfo_y() + step)))
bbutt.pack()
bbutt.place(x = 350, y = 650)

lbutt = Button(text="<", command = lambda : (lmao.place(x = lmao.winfo_x() - step, y = lmao.winfo_y())))
lbutt.pack()
lbutt.place(x = 300, y = 650)

root.mainloop()