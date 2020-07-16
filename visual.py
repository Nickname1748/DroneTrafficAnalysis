import tkinter

def init_window():
    window = tkinter.Tk()
    return window

def init_canvas(window):
    canvas = tkinter.Canvas(window, bg='gray', width=1640, height=1640)
    canvas.create_rectangle(10, 10, 1630, 1630, fill='white')

    for i in range(8):
        for j in range(8):
            canvas.create_rectangle(200*i + 30, 200*j + 30, 200*i + 210, 200*j + 210, fill='gray')

    canvas.pack()
    return canvas

def end(window):
    window.mainloop()
