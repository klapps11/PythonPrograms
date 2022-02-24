import tkinter
import mywidget


root = tkinter.Tk()

# Title Label
label = tkinter.Label(root, text='Custom Widget Using Method')
label.pack()

# Custom Widget 1
myWidget1 = mywidget.MyWidget(root, 'My Widget 1')
myWidget1.pack()

# Custom Widget 2
myWidget2 = mywidget.MyWidget(root, 'My Widget 2')
myWidget2.pack()

root.mainloop()
