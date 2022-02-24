import tkinter
import tkinter.filedialog
import frequently_used


class Add:
    def __init__(self, master, target):
        
        self.target = target
        self.master = master
        self.nameLabel = tkinter.Label(master, text='Name: ')
        self.nameEntry = tkinter.Entry(master)
        self.pathLabel = tkinter.Label(master, text='Path: ')
        self.pathEntry = tkinter.Entry(master)
        self.pathChooser = tkinter.Button(master, text='Choose Path', command=self.choosePath)
        self.okButton = tkinter.Button(master, text='OK')
        self.okButton['command'] = self.getAttributes
        self.nameLabel.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1, columnspan=2)
        self.pathLabel.grid(row=1, column=0)
        self.pathEntry.grid(row=1, column=1)
        self.pathChooser.grid(row=1, column=2)
        self.okButton.grid(row=2, column=0, columnspan=3)

    def choosePath(self):
        self.pathEntry.delete(0, tkinter.END)
        if self.target == 'file':
            self.pathEntry.insert(0, tkinter.filedialog.askopenfilename())
        if self.target == 'dir':
            self.pathEntry.insert(0, tkinter.filedialog.askdirectory())

    def getAttributes(self):
        frequently_used.updateFile(self.nameEntry.get(),self.pathEntry.get(), self.target)
        self.master.destroy()
