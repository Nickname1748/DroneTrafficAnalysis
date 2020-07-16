import visual
import algorythm

window = visual.init_window()
canvas = visual.init_canvas(window)

algorythm.init_matrix(5, 81)
algorythm.create_car()

visual.end(window)
