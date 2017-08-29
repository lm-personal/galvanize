#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from gui2 import Hello

# In more complex GUIs,
# we might instead attach large Frame subclasses to other container components
# and develop each independently.
class HelloContainer(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):

        # Attach Hello to HelloContainer
        Hello(self).pack(side=RIGHT)

        # Attach another Button to HelloContainer
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    HelloContainer().mainloop()
