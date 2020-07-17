import tkinter
import time

def init_window():
    '''
    Initialize main window.
    '''

    window = tkinter.Tk()
    window.title('DroneTrafficAnalysis')
    window.resizable(False, False)
    return window

def init_canvas(window):
    '''
    Initialize main canvas and roads.
    '''

    canvas = tkinter.Canvas(window, bg='gray', width=1640, height=1640)
    canvas.create_rectangle(10, 10, 1630, 1630, fill='white')

    for i in range(8):
        for j in range(8):
            canvas.create_rectangle(200*i + 30, 200*j + 30, 200*i + 210, 200*j + 210, fill='gray')

    canvas.pack()
    return canvas

def display_path(canvas, Points):
    '''
    Display canvas path.
    '''

    pts = [item for point in Points for item in point]
    canvas.create_line(*pts, width=3, fill='gray')

def animate_cars(canvas, MPaths, Times):
    '''
    Animate all movements of cars.
    '''

    timer = 0
    CarModels = []
    for i in range(len(MPaths)):
        CarModels.append(canvas.create_oval(-10, -10, 0, 0, fill='black'))
    while(True):
        stop = True
        for i in range(len(CarModels)):
            if len(MPaths[i]) > 0:
                stop = False
                if timer >= Times[i]:
                    canvas.move(CarModels[i], *MPaths[i][0])
                    MPaths[i].pop(0)
        if stop:
            break
        canvas.update()
        timer += 1
        time.sleep(0.02)




def end(window):
    '''
    Main loop.
    '''

    window.mainloop()
