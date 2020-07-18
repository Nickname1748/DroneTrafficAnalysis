import random

class Car:
    '''
    Car object represents one individual car simulation.
    '''

    def __init__(self, speed, origin, dest):
        '''
        Initialize a Car class instance with basic attiributes.
        '''

        self.speed = speed
        self.origin = origin
        self.dest = dest

    def route(self, Matrix, nodes):
        '''
        Generate efficient path from origin to destination.
        '''

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

    def set_points(self):
        '''
        Generate simple canvas path from route.
        '''

        Route = self.Route
        Points = []
        init_coords = place_to_coords(self.origin)
        Points.append(init_coords)

        init_coords = list(init_coords)
        side = self.origin[2]
        if side == 0:
            init_coords[1] -= 15
        elif side == 1:
            init_coords[0] += 15
        elif side == 2:
            init_coords[1] += 15
        else:
            init_coords[0] -= 15
        Points.append(tuple(init_coords))

        for node in Route:
            Points.append(node_to_coords(node))

        init_coords = list(place_to_coords(self.dest, reverse=True))
        side = self.dest[2]
        if side == 0:
            init_coords[0] += 15
        elif side == 1:
            init_coords[1] += 15
        elif side == 2:
            init_coords[0] -= 15
        else:
            init_coords[1] -= 15
        Points.append(tuple(init_coords))

        Points.append(place_to_coords(self.dest, reverse=True))

        TPoints = []
        Dirs = []
        for i in range(len(Points)-1):
            if Points[i][0] == Points[i+1][0]: # X Static
                if Points[i][1] < Points[i+1][1]: # Moving Down
                    Dirs.append(2)
                else: # Moving Up
                    Dirs.append(0)
            else: # Y Static
                if Points[i][0] < Points[i+1][0]: # Moving Right
                    Dirs.append(1)
                else: # Moving Left
                    Dirs.append(3)

        if Dirs[0] == 0: # Up
            TPoints.append((Points[0][0] + 5, Points[0][1]))
        elif Dirs[0] == 1: # Right
            TPoints.append((Points[0][0], Points[0][1] + 5))
        elif Dirs[0] == 2: # Down
            TPoints.append((Points[0][0] - 5, Points[0][1]))
        else: # Left
            TPoints.append((Points[0][0], Points[0][1] - 5))

        for i in range(len(Dirs) - 1):
            if Dirs[i] == Dirs[i+1]:
                if Dirs[i] == 0: # Up
                    TPoints.append((Points[i+1][0] + 5, Points[i+1][1]))
                elif Dirs[i] == 1: # Right
                    TPoints.append((Points[i+1][0], Points[i+1][1] + 5))
                elif Dirs[i] == 2: # Down
                    TPoints.append((Points[i+1][0] - 5, Points[i+1][1]))
                else: # Left
                    TPoints.append((Points[i+1][0], Points[i+1][1] - 5))
            elif Dirs[i] == 0 or Dirs[i] == 2: # Up or Down
                if Dirs[i+1] == 1: # Right
                    TPoints.append((TPoints[-1][0], Points[i+1][1] + 5))
                elif Dirs[i+1] == 3: # Left
                    TPoints.append((TPoints[-1][0], Points[i+1][1] - 5))
                elif Dirs[i+1] == 0: # Up
                    TPoints.append((TPoints[-1][0], Points[i+1][1] + 5))
                    TPoints.append((TPoints[-1][0] + 10, Points[i+1][1] + 5))
                else: # Down
                    TPoints.append((TPoints[-1][0], Points[i+1][1] - 5))
                    TPoints.append((TPoints[-1][0] - 10, Points[i+1][1] - 5))
            else: # Left or Right
                if Dirs[i+1] == 0: # Up
                    TPoints.append((Points[i+1][0] + 5, TPoints[-1][1]))
                elif Dirs[i+1] == 2: # Down
                    TPoints.append((Points[i+1][0] - 5, TPoints[-1][1]))
                elif Dirs[i+1] == 1: # Right
                    TPoints.append((Points[i+1][0] - 5, TPoints[-1][1]))
                    TPoints.append((Points[i+1][0] - 5, TPoints[-1][1] + 10))
                else: # Left
                    TPoints.append((Points[i+1][0] + 5, TPoints[-1][1]))
                    TPoints.append((Points[i+1][0] + 5, TPoints[-1][1] - 10))

        if Dirs[-1] == 0: # Up
            TPoints.append((Points[-1][0] + 5, Points[-1][1]))
        elif Dirs[-1] == 1: # Right
            TPoints.append((Points[-1][0], Points[-1][1] + 5))
        elif Dirs[-1] == 2: # Down
            TPoints.append((Points[-1][0] - 5, Points[-1][1]))
        else: # Left
            TPoints.append((Points[-1][0], Points[-1][1] - 5))

        self.TPoints = TPoints

    def get_points(self):
        '''
        Get simple canvas path from Car instance.
        '''

        return self.TPoints
    
    def set_movement_points(self):
        '''
        Generate detailed canvas path for Car from simple path.
        '''

        TPoints = self.TPoints

        MPoints = []
        for i in range(len(TPoints)-1):
            X, Y = [], []
            if TPoints[i][0] == TPoints[i+1][0]:
                if TPoints[i][1] < TPoints[i+1][1]:
                    Y = list(range(TPoints[i][1], TPoints[i+1][1], self.speed))
                    Y.append(TPoints[i+1][1])
                else:
                    Y = list(range(TPoints[i][1], TPoints[i+1][1], -self.speed))
                    Y.append(TPoints[i+1][1])
                X = [TPoints[i][0]]*len(Y)
            else:
                if TPoints[i][0] < TPoints[i+1][0]:
                    X = list(range(TPoints[i][0], TPoints[i+1][0], self.speed))
                    X.append(TPoints[i+1][0])
                else:
                    X = list(range(TPoints[i][0], TPoints[i+1][0], -self.speed))
                    X.append(TPoints[i+1][0])
                Y = [TPoints[i][1]]*len(X)
            MPoints.extend(zip(X, Y))

        self.MPoints = MPoints

    def get_movement_points(self):
        '''
        Get detailed canvas path from Car instance.
        '''

        return self.MPoints
    
    def set_movement_offsets(self):
        '''
        Generate detailed frame movements for Car from detailed canvas path.
        '''

        MPoints = self.MPoints
        MOffsets = []
        MOffsets.append(tuple((MPoints[0][0]+5, MPoints[0][1]+5)))
        for i in range(1, len(MPoints)):
            MOffsets.append(tuple((MPoints[i][0]-MPoints[i-1][0], MPoints[i][1]-MPoints[i-1][1])))
        self.MOffsets = MOffsets
    
    def get_movement_offsets(self):
        '''
        Get detailed frame movements from Car instance.
        '''

        return self.MOffsets

def place_to_id(place):
    '''
    Convert place to nearest node ID.
    '''

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

def place_to_coords(place, reverse=False):
    '''
    Convert place to its canvas coordinates.
    '''

    row = place[0]
    col = place[1]
    side = place[2]

    x = 120 + 200*col
    y = 120 + 200*row

    if reverse:
        if side == 0:
            x += 85
        elif side == 1:
            y += 85
        elif side == 2:
            x -= 85
        else:
            y -= 85
    else:
        if side == 0:
            y -= 85
        elif side == 1:
            x += 85
        elif side == 2:
            y += 85
        else:
            x -= 85
    
    return (x, y)

def node_to_coords(id):
    '''
    Convert node ID to its canvas coordinates.
    '''

    row = id // 9
    col = id % 9
    
    x = 20 + 200*col
    y = 20 + 200*row

    return (x, y)

def rand_place():
    '''
    Generates random place.
    '''

    row = random.randint(0, 7)
    col = random.randint(0, 7)
    side = random.randint(0, 3)
    return (row, col, side)

Matrix = []
Cars = []

def init_matrix(weight, nodes):
    '''
    Initialize matrix of road graph.
    '''

    global Matrix

    for i in range(nodes):
        Row = [1000000]*nodes

        if i >= 9: # Up
            Row[i - 9] = 5

        if i < 72: # Down
            Row[i + 9] = 5

        if i%9 != 0: # Left
            Row[i - 1] = 5

        if i%9 != 8: # Right
            Row[i + 1] = 5

        Matrix.append(Row)

def create_car():
    '''
    Creates new Car instance, calculate its paths, and add it to common list.
    '''

    speed = random.randint(2, 4)
    origin = rand_place()
    dest = rand_place()
    new_car = Car(speed, origin, dest)
    global Matrix
    Matrix = new_car.route(Matrix, 81)
    new_car.set_points()
    new_car.set_movement_points()
    new_car.set_movement_offsets()
    Cars.append(new_car)

def get_cars():
    '''
    Get list of Car instances.
    '''
    
    return Cars
