#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from tkinter import *
from tkinter.messagebox import showinfo
import csv


class lookup_gui(Frame):



    def __init__(self, parent=None):

        Frame.__init__(self, parent)
        self.data_file = "data.csv"
        self.entries = {}
        self.pack()
        self.makeWidgets()



    def makeWidgets(self):

        for index, value in enumerate(fieldnames):
            label = Label(self, text=value)
            entry = Entry(self)
            label.grid(row=index, column=0)
            entry.grid(row=index, column=1)
            self.entries[value] = entry

        Button(self, text="Fetch", command=self.fetchRecord).grid(row=index+1, column=0)
        Button(self, text="Update", command=quit).grid(row=index+1, column=1)
        Button(self, text="Quit", command=quit).grid(row=index+1, column=2)



    def fetchRecord(self):

        name = self.entries['first_name'].get() + self.entries['last_name'].get()

        with open(self.data_file) as data:

            reader = csv.DictReader(data)
            for row in reader:

                entry_name = row['first_name'] + row['last_name']
                if entry_name == name:
                    for field in fieldnames:
                        self.entries[field].delete(0, END)
                        self.entries[field].insert(0, row[field])



class top(Frame):

    def __init__(self, parent=None):
        
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):

        lookup_gui()



fieldnames = ['first_name', 'last_name', 'school', 'position', 'height', 'weight', '40time', 'bench', 'vert', 'broad', 'shuttle', '3cone']

root = Tk()
root.title('DraftDB')
top(root).pack()
root.mainloop()
