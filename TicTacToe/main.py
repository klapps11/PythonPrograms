import tkinter
import tictactoe


def reset():
    global c
    for i in range(9):
        b[i].config(text='', state=tkinter.ACTIVE)
    c = 0
    status.config(text='X\'s turn')
    tictactoe.reset()


root = tkinter.Tk()
root.title('Tic Tac Toe')
root.geometry('495x575')
status = tkinter.Label(root, text='X\'s turn', font=('', 20))
reset = tkinter.Button(root, text='Reset', command=reset, font=('', 20), width=10, bg='gray')
b = []
c = 0
for i in range(3):
    for j in range(3):
        b.append(tictactoe.TicTacToe(root, number=c, status=status, width=3, text='', font=('', 66)))
        b[c].grid(row=i, column=j)
        c += 1
status.grid(row=3, column=0, columnspan=2)
reset.grid(row=3, column=2, columnspan=1)
root.mainloop()
