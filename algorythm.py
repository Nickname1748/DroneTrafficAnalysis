import random

class Car:
    def __init__(self, speed, origin, dest):
        self.speed = speed
        self.origin = origin
        self.dest = dest

    def route(self, Matrix, nodes):
        Weight = [1000000]*nodes
        Visited = [False]*nodes

        origin = place_to_id(self.origin)
        dest = place_to_id(self.dest)

        Nearest = [origin for i in range(nodes)]
        Weight[origin] = 0
        current = origin

        for k in range(nodes):
            Visited[current] = True

            for i in range(nodes):
                if not Visited[i] and (Weight[current]
                                    + Matrix[current][i] < Weight[i]):
                    Weight[i] = Weight[current] + Matrix[current][i]
                    Nearest[i] = current

            min_i = -1
            min_x = 1000000

            for i in range(nodes):
                if not Visited[i] and Weight[i] < min_x:
                    min_i = i
                    min_x = Weight[i]
            current = min_i

        Route = [dest]
        current = dest

        while current != origin:
            Route.insert(0, Nearest[current])
            Matrix[Nearest[current]][current] += 2
            current = Nearest[current]
        self.Route = Route

        return Matrix

def place_to_id(place):
    row, col, side = place[0], place[1], place[2]

    if side == 0:
        i, j = row, col + 1

    elif side == 1:
        i, j = row + 1, col + 1

    elif side == 2:
        i, j = row + 1, col

    else:
        i, j = row, col

    id = i*9 + j
    return id

def rand_place():
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    side = random.randint(0, 3)
    return (row, col, side)

Matrix = []
Cars = []

def init_matrix(weight, nodes):
    global Matrix

    for i in range(nodes):
        Row = [1000000]*nodes

        if i >= 9:
            Row[i - 9] = 5

        if i < 72:
            Row[i + 9] = 5

        if i%9 != 0:
            Row[i - 1] = 5

        if i%9 != 8:
            Row[i + 1] = 5

        Matrix.append(Row)

def create_car():
    speed = random.randint(2, 4)
    origin = rand_place()
    dest = rand_place()
    new_car = Car(speed, origin, dest)

    global Matrix
    Matrix = new_car.route(Matrix, 81)
