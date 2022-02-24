import tkinter


class MyWidget(tkinter.Frame):
    def __init__(self, master, text):
        super().__init__(master)

        self.label = tkinter.Label(self, text=text)
        self.btn = tkinter.Button(self, text=self.label['text'])
        self.btn['command'] = lambda: print(self.label['text'])
        self.label.grid(row=0, column=0)
        self.btn.grid(row=0, column=1)
