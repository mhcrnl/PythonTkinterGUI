#!/usr/bin/python
from Tkinter import *
from tkFileDialog import *

def show_entry_fields():
   print("Data: %s\n"
         "Index apa rece bucatarie: %s\n" 
         "Index apa calda bucatarie: %s\n"
         "Index apa rece baie: %s\n"
         "Index apa calda baie: %s\n"
         "Gaze: %s\n" % (data.get(), iarbuc.get(), iacbuc.get(), iarbai.get(),
                                         iacbai.get(), gaze.get()))

def NewFile():
    print "new file"

def OpenFile():
    name= askopenfilename()
    print name

def About():
    #about=showinfo()
    print "about"

def Quit():
    #print "quit"
    #import sys; sys.exit()
    master.destroy

def Save():
    text = "Data: %s\nIndex apa rece bucatarie: %s\nIndex apa calda bucatarie: %s\n" % (data.get(), iarbuc.get(), iacbuc.get())
    with open ("text.txt", "a") as f:
        f.write(text)
    print "save"

master = Tk()
master.title("Index Contori")

v = StringVar()

menu= Menu(master)
master.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open..", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.destroy)

helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About..", command=About)

Label(master, text="Data").grid(row=0)
Label(master, text="Index apa rece bucatarie").grid(row=1)
Label(master, text="Index apa calda bucatarie").grid(row=2)
Label(master, text="Index apa rece baie").grid(row=3)
Label(master, text="Index apa calda baie").grid(row=4)
Label(master, text="Gaze").grid(row=5)

data = Entry(master, bd=5)
iarbuc = Entry(master, textvariable=v, bd=5)
iacbuc = Entry(master, bd=5)
iarbai = Entry(master, bd=5)
iacbai = Entry(master, bd=5)
gaze = Entry(master, bd=5)

data.  grid(row=0, column=1)
iarbuc.grid(row=1, column=1)
iacbuc.grid(row=2, column=1)
iarbai.grid(row=3, column=1)
iacbai.grid(row=4, column=1)
gaze.  grid(row=5, column=1)

Button(master, text='Quit', command=master.destroy).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=7, column=1, sticky=W, pady=4)
Button(master, text='Save', command=Save).grid(row=7, column=2, sticky=W, pady=4)
mainloop( )

