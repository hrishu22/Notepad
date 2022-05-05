from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import os
root=Tk()
def new():
    textarea.delete(1.0, END)
    root.title("Untittle-Thinkpad")
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-ThinkPad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close
def savefile():from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
from tkinter.messagebox import showinfo
import os
root=Tk()
def new():
    textarea.delete(1.0, END)
    root.title("Untittle-Thinkpad")
def clear():
    textarea.event_generate(("<<Clear>>"))
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-ThinkPad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close
def savefile():
    file = asksaveasfile(initialfile='Untittle-ThinkPad',mode='w', defaultextension='.txt')
    if file!= None:
        data = textarea.get('1.0', END)
    try:
        file.write(data)
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")
def saveas():
    fd = asksaveasfile(mode='w', defaultextension = '.txt')
    t = textarea.get(0.0, END)
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
def exit():
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))
root.title("Untittled- Notepad")
root.geometry("500x500")
root.minsize(200,200)
textarea=Text(root, font="lucida 18")
textarea.pack(expand=True, fill=BOTH)
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
textarea.config(yscrollcommand=scroll.set)
scroll.config(command=textarea.yview)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Save As",command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Clear",command=clear)
filemenu.add_command(label="Quit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


root.mainloop()
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untittle-ThinkPad',filetypes=[("All Files","*.*"),"Txt Documents","*.txt"])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))
root.title("Untittled- Notepad")
root.geometry("500x500")
root.minsize(200,200)
root.iconbitmap("1.ico")
textarea=Text(root, font="lucida 18")
textarea.pack(expand=True, fill=BOTH)
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
textarea.config(yscrollcommand=scroll.set)
scroll.config(command=textarea.yview)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Clear")
filemenu.add_command(label="Quit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


root.mainloop()
