import visual
import algorythm

window = visual.init_window()
canvas = visual.init_canvas(window)

algorythm.init_matrix(weight=5)
for i in range(5):
    algorythm.create_car()
Cars = algorythm.get_cars()

MPaths = []
Times = []

for car in Cars:
    visual.draw_path(canvas, car.get_points())
    MPaths.append(car.get_movement_offsets())
    Times.append(0)

visual.animate_cars(canvas, MPaths, Times)

visual.end(window)