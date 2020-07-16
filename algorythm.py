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

    def set_points(self):
        Route = self.Route
        Points = []
        init_coords = place_to_coords(self.origin)
        Points.append(init_coords)

        init_coords = list(init_coords)
        side = self.origin[2]
        if side == 0:
            init_coords[1] -= 10
        elif side == 1:
            init_coords[0] += 10
        elif side == 2:
            init_coords[1] += 10
        else:
            init_coords[0] -= 10
        Points.append(tuple(init_coords))

        for node in Route:
            Points.append(node_to_coords(node))

        init_coords = list(place_to_coords(self.dest, reverse=True))
        side = self.dest[2]
        if side == 0:
            init_coords[0] += 10
        elif side == 1:
            init_coords[1] += 10
        elif side == 2:
            init_coords[0] -= 10
        else:
            init_coords[1] -= 10
        Points.append(tuple(init_coords))

        Points.append(place_to_coords(self.dest, reverse=True))
        self.Points = Points

    def get_points(self):
        return self.Points
    
    def set_movement_points(self):
        Points = self.Points
        MPoints = []
        for i in range(len(Points)-1):
            X, Y = [], []
            if Points[i][0] == Points[i+1][0]:
                if Points[i][1] < Points[i+1][1]:
                    Y = list(range(Points[i][1], Points[i+1][1], self.speed))
                    X = [Points[i][0]-5]*len(Y)
                else:
                    Y = list(range(Points[i][1], Points[i+1][1], -self.speed))
                    X = [Points[i][0]+5]*len(Y)
            else:
                if Points[i][0] < Points[i+1][0]:
                    X = list(range(Points[i][0], Points[i+1][0], self.speed))
                    Y = [Points[i][1]+5]*len(X)
                else:
                    X = list(range(Points[i][0], Points[i+1][0], -self.speed))
                    Y = [Points[i][1]-5]*len(X)
            MPoints.extend(zip(X, Y))
        self.MPoints = MPoints

    def get_movement_points(self):
        return self.MPoints
    
    def set_movement_offsets(self):
        MPoints = self.MPoints
        MOffsets = []
        MOffsets.append(tuple((MPoints[0][0]+5, MPoints[0][1]+5)))
        for i in range(1, len(MPoints)):
            MOffsets.append(tuple((MPoints[i][0]-MPoints[i-1][0], MPoints[i][1]-MPoints[i-1][1])))
        self.MOffsets = MOffsets
    
    def get_movement_offsets(self):
        return self.MOffsets

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

def place_to_coords(place, reverse=False):
    row = place[0]
    col = place[1]
    side = place[2]

    x = 120 + 200*col
    y = 120 + 200*row

    if reverse:
        if side == 0:
            x += 90
        elif side == 1:
            y += 90
        elif side == 2:
            x -= 90
        else:
            y -= 90
    else:
        if side == 0:
            y -= 90
        elif side == 1:
            x += 90
        elif side == 2:
            y += 90
        else:
            x -= 90
    
    return (x, y)

def node_to_coords(id):
    row = id // 9
    col = id % 9
    
    x = 20 + 200*col
    y = 20 + 200*row

    return (x, y)

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
    new_car.set_points()
    new_car.set_movement_points()
    new_car.set_movement_offsets()
    Cars.append(new_car)

def get_cars():
    return Cars