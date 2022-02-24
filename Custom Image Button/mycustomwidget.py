import tkinter
from PIL import ImageTk, Image


class MyButton(tkinter.Button):
    def __init__(self, master, btnUpFilePath, btnDownFilePath, size=100, **kw):
        super().__init__(master, **kw)

        (self.width, self.height) = Image.open(btnUpFilePath).size
        self.width = int(self.width*(size / 100))
        self.height = int(self.height*(size / 100))
        
        self.btnUpFile = Image.open(btnUpFilePath).resize((self.width, self.height))
        self.btnDownFile = Image.open(btnDownFilePath).resize((self.width, self.height))
        self.btnUpFile = ImageTk.PhotoImage(self.btnUpFile)
        self.btnDownFile = ImageTk.PhotoImage(self.btnDownFile)
        self['image'] = self.btnUpFile
        self.bind('<Button>', self.btnDown)
        self.bind('<ButtonRelease>', self.btnUp)

    def btnDown(self, event):
        self.config(image=self.btnDownFile)

    def btnUp(self, event):
        self.config(image=self.btnUpFile)
