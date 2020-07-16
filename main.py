import visual
import algorythm

window = visual.init_window()
canvas = visual.init_canvas(window)

algorythm.init_matrix(weight=5)
algorythm.create_car()
Cars = algorythm.get_cars()

for car in Cars:
    visual.draw_path(canvas, car.get_points())

visual.end(window)