import random

class Car:
    def __init__(self, speed, origin, dest):
        self.speed = speed
        self.origin = origin
        self.dest = dest
    
    def route(self, Matrix):
        Weight = [1000000]*81
        Visited = [False]*81
        origin = place_to_id(self.origin)
        dest = place_to_id(self.dest)
        Nearest = []
        for i in range(81):
            Nearest.append(origin)
        Weight[origin] = 0
        current = origin
        for k in range(81):
            Visited[current] = True
            for i in range(81):
                if not Visited[i]:
                    if Weight[current]+Matrix[current][i] < Weight[i]:
                        Weight[i] = Weight[current]+Matrix[current][i]
                        Nearest[i] = current
            mini = -1
            minx = 1000000
            for i in range(81):
                if Weight[i] < minx and not Visited[i]:
                    mini = i
                    minx = Weight[i]
            current = mini
        Route = [dest]
        current = dest
        while current != origin:
            Route.insert(0, Nearest[current])
            Matrix[Nearest[current]][current] += 2
            current = Nearest[current]
        self.Route = Route
        return Matrix

def place_to_id(place):
    row = place[0]
    col = place[1]
    side = place[2]

    if side == 0:
        i = row
        j = col+1
    elif side == 1:
        i = row+1
        j = col+1
    elif side == 2:
        i = row+1
        j = col
    else:
        i = row
        j = col
    
    id = i*9 + j
    return id

def rand_place():
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    side = random.randint(0, 3)
    return (row, col, side)

Matrix = []

Cars = []

def init_matrix(weight):
    global Matrix
    for i in range(81):
        Row = [1000000]*81
        if(i >= 9):
            Row[i-9] = 5
        if(i < 72):
            Row[i+9] = 5
        if(i%9 != 0):
            Row[i-1] = 5
        if(i%9 != 8):
            Row[i+1] = 5
        Matrix.append(Row)

def create_car():
    speed = random.randint(2, 4)
    origin = rand_place()
    dest = rand_place()
    new_car = Car(speed, origin, dest)
    global Matrix
    Matrix = new_car.route(Matrix)