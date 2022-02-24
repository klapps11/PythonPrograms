import tkinter
import mycustomwidget

def btnClk():
    print('Button Clicked')


root = tkinter.Tk()
root.geometry('512x288')  # Optional

button = mycustomwidget.MyButton(root, 'buttonUp.png', 'buttonDown.png', 75, command=btnClk)
button.pack()

root.mainloop()
