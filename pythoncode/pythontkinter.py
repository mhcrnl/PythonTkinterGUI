#!/usr/bin/python
from Tkinter import *
from tkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Label(text="Index apa Rece Bucatarie").pack(fill=X)
e1=Entry()
e1.pack(fill=X)
Label(text="Index apa calda Bucatarie").pack(fill=X)
iacbuc=Entry()
iacbuc.pack(fill=X)
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()
