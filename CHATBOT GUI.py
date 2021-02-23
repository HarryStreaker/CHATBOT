from tkinter import *
root= Tk()

txt = Text(root)
txt.grid(row = 0, column = 0, columnspan = 2)

e = Entry(root,width=100)

send = Button(root, text="Send").grid(row=1, column=1)

e.grid(row = 1, column = 0)

root.title("CHATBOT")
root.mainloop()