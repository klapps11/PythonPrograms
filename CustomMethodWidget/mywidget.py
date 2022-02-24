import tkinter


def MyWidget(master, text):
    frame = tkinter.Frame(master)

    label = tkinter.Label(frame, text=text)
    btn = tkinter.Button(frame, text=label['text'])
    btn['command'] = lambda: print(label['text'])
    label.grid(row=0, column=0)
    btn.grid(row=0, column=1)

    return frame
