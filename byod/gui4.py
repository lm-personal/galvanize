#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from tkinter.messagebox import showinfo



class name_echo(Frame):
    
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):

        label = Label(self, text="Enter Your Name:")
        label.pack(side='top')
        text_field = Entry(self)
        text_field.pack(side='top')
        submit = Button(self, text="Submit", command=(lambda: self.echo(text_field.get())))
        submit.pack(side=TOP)

    def echo(self, name):
        showinfo(title='Reply', message='Hello {}!'.format(name))



class top(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):

        name_echo()



root = Tk()
root.title('ExProg')
top(root).pack()
root.mainloop()
