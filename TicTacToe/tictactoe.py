import tkinter

count = 0
xPos = []
oPos = []
buttonsArray = []


def reset():
    global count, xPos, oPos
    count = 0
    xPos = []
    oPos = []


def result(status):
    if count < 5:
        return
    if (1 in xPos and 2 in xPos and 3 in xPos)\
            or (4 in xPos and 5 in xPos and 6 in xPos)\
            or (7 in xPos and 8 in xPos and 9 in xPos)\
            or (1 in xPos and 4 in xPos and 7 in xPos)\
            or (2 in xPos and 5 in xPos and 8 in xPos)\
            or (3 in xPos and 6 in xPos and 9 in xPos)\
            or (1 in xPos and 5 in xPos and 9 in xPos)\
            or (3 in xPos and 5 in xPos and 7 in xPos):
        print('X wins!')
        status['text'] = 'X Wins!'
        for i in range(9):
            buttonsArray[i].config(state=tkinter.DISABLED)

    if (1 in oPos and 2 in oPos and 3 in oPos)\
            or (4 in oPos and 5 in oPos and 6 in oPos)\
            or (7 in oPos and 8 in oPos and 9 in oPos)\
            or (1 in oPos and 4 in oPos and 7 in oPos)\
            or (2 in oPos and 5 in oPos and 8 in oPos)\
            or (3 in oPos and 6 in oPos and 9 in oPos)\
            or (1 in oPos and 5 in oPos and 9 in oPos)\
            or (3 in oPos and 5 in oPos and 7 in oPos):
        print('O wins!')
        status['text'] = 'O Wins!'
        for i in range(9):
            buttonsArray[i].config(state=tkinter.DISABLED)

    if count == 9:
        print('Draw!')
        status['text'] = 'Draw!'


class TicTacToe(tkinter.Button):
    def __init__(self, master, number, status, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.number = number
        self.status = status
        self.config(command=self.btnClk)
        buttonsArray.append(self)

    def btnClk(self):
        global count, xPos, oPos
        if count % 2 == 0:
            self.config(text='X')
            self.config(state=tkinter.DISABLED)
            xPos.append(self.number + 1)
            self.status['text'] = 'O\'s turn'
            count += 1
            result(self.status)

        else:
            self.config(text='O')
            self.config(state=tkinter.DISABLED)
            oPos.append(self.number + 1)
            self.status['text'] = 'X\'s turn'
            count += 1
            result(self.status)
