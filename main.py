import visual
import algorithm

window = visual.init_window()
canvas = visual.init_canvas(window)

algorithm.init_matrix(5, 81)
for i in range(100):
    algorithm.create_car()
Cars = algorithm.get_cars()

MPaths = []
Times = []

for car in Cars:
    visual.display_path(canvas, car.get_points())
    MPaths.append(car.get_movement_offsets())
    Times.append(0)

visual.animate_cars(canvas, MPaths, Times)

visual.end(window)
