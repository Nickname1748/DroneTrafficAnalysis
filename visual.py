import tkinter

def init_window():
    window = tkinter.Tk()
    return window

def init_canvas(window):
    canvas = tkinter.Canvas(window, bg='gray', width=1640, height=1640)
    field = canvas.create_rectangle(10, 10, 1630, 1630, fill='white')
    for i in range(8):
        for j in range(8):
            canvas.create_rectangle(200*i+30, 200*j+30, 200*i+210, 200*j+210, fill='gray')
    canvas.pack()
    return canvas

def draw_path(canvas, Points):
    pts = [item for point in Points for item in point]
    canvas.create_line(*pts, width=3)

def end(window):
    window.mainloop()