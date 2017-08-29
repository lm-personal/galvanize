#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *

# Frame widgets are just containers for other widgets,
# and so give rise to the notion of GUIs as widget hierarchies, or trees.
#I n general by attaching widgets to frames,
# and frames to other frames, we can build up arbitrary GUI layouts.
# Simply divide the user interface into a set of increasingly smaller rectangles,
# implement each as a tkinter Frame,
# and attach basic widgets to the frame in the desired screen position.
class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):

        # Button will run the argument passed to command when pressed
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)

if __name__ == '__main__':
    Hello().mainloop()
