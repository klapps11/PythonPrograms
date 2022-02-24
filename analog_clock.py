import datetime
import math
import tkinter

root = tkinter.Tk()
size = 256
root.geometry(str(size) + 'x' + str(size))
cx = cy = size/2

deg = 90
sLen = 100
mLen = 75
hLen = 50


def deg2rad(degree):
    return (math.pi / 180) * degree


def refresher():
    canvas.delete('all')

    # (x, y) = ((len*cos(angle)) + cx, (len*sin(angle)) + cy)

    s = datetime.datetime.now().second
    sx = sLen * math.cos(deg2rad((s * 6) - deg)) + cx
    sy = sLen * math.sin(deg2rad((s * 6) - deg)) + cy
    canvas.create_line(cx, cy, sx, sy)

    m = datetime.datetime.now().minute
    mx = mLen * math.cos(deg2rad((m * 6) - deg)) + cx
    my = mLen * math.sin(deg2rad((m * 6) - deg)) + cy
    canvas.create_line(cx, cy, mx, my)

    h = datetime.datetime.now().hour
    hx = hLen * math.cos(deg2rad((h * 30) - deg)) + cx
    hy = hLen * math.sin(deg2rad((h * 30) - deg)) + cy
    canvas.create_line(cx, cy, hx, hy)

    root.after(1000, refresher)


canvas = tkinter.Canvas(root)
canvas.pack()
refresher()
root.mainloop()
