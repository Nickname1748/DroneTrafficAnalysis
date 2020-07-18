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
    Coords = [(-5, -5)]*len(MPaths)
    for i in range(len(MPaths)):
        CarModels.append(canvas.create_oval(-10, -10, 0, 0, fill='black'))
    while(True):
        stop = True
        for i in range(len(CarModels)):
            if len(MPaths[i]) > 0:
                stop = False
                if timer >= Times[i]:
                    curr_coord = Coords[i]
                    new_coord = (curr_coord[0] + MPaths[i][0][0], curr_coord[1] + MPaths[i][0][1])
                    free = True
                    if ((curr_coord[0] % 200 <= 5 or curr_coord[0] % 200 >= 35
                            or curr_coord[1] % 200 <= 5 or curr_coord[1] % 200 >= 35)
                            and (new_coord[0] % 200 > 5 and new_coord[0] % 200 < 35
                            and new_coord[1] % 200 > 5 and new_coord[1] % 200 < 35)):
                        for j in range(len(Coords)):
                            if i == j:
                                continue
                            cross_x = new_coord[0] // 200
                            cross_y = new_coord[1] // 200
                            coord = Coords[j]
                            if (coord[0] > 200*cross_x + 5 and coord[0] < 200*cross_x + 35
                                    and coord[1] > 200*cross_y + 5 and coord[1] < 200*cross_y + 35):
                                free = False
                                break
                    else:
                        for j in range(len(Coords)):
                            if i == j:
                                continue
                            coord = Coords[j]
                            if abs(coord[0] - new_coord[0]) < 10 and abs(coord[1] - new_coord[1]) < 10:
                                free = False
                                break
                    if free:
                        canvas.move(CarModels[i], *MPaths[i][0])
                        Coords[i] = new_coord
                        MPaths[i].pop(0)
            else:
                Movement = (-Coords[i][0] - 5, -Coords[i][1] - 5)
                canvas.move(CarModels[i], *Movement)
                Coords[i] = (-5, -5)
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
