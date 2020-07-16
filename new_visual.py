import tkinter

def init_window():
    window = tkinter.Tk()
    return window

def get_size(house_len):
    return 110 + house_len * 8

def init_canvas(window, house_len):
    length = get_size(house_len)
    canvas = tkinter.Canvas(window, width = length, height = length, bg = 'grey')
    canvas.create_rectangle(10, 10, length - 10, length - 10, fill = 'white')
    for i in range(8):
        for j in range(8):
            canvas.create_rectangle((house_len + 10) * i + 20, (house_len + 10) * j + 20, (house_len + 10) * i + house_len + 20, (house_len + 10) * j + house_len + 20, fill = 'grey')
    canvas.pack()
    return canvas

window = init_window()
init_canvas(window, 40)
window.mainloop()