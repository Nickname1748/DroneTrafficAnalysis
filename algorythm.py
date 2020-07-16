import random

class Car:
    def __init__(self, speed, origin, dest):
        self.speed = speed
        self.origin = origin
        self.dest = dest
    
    def route(self, M):
        W = [1000000]*81
        V = [False]*81
        origin = place_to_id(self.origin)
        dest = place_to_id(self.dest)
        N = []
        for i in range(81):
            N.append(origin)
        W[origin] = 0
        current = origin
        for k in range(81):
            V[current] = True
            for i in range(81):
                if not V[i]:
                    if W[current]+M[current][i] < W[i]:
                        W[i] = W[current]+M[current][i]
                        N[i] = current
            mini = -1
            minx = 1000000
            for i in range(81):
                if W[i] < minx and not V[i]:
                    mini = i
                    minx = W[i]
            current = mini
        R = [dest]
        current = dest
        while current != origin:
            R.insert(0, N[current])
            M[N[current]][current] += 2
            current = N[current]
        self.R = R
        return M

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

M = []

Cars = []

def init_matrix(weight):
    global M
    for i in range(81):
        R = [1000000]*81
        if(i >= 9):
            R[i-9] = 5
        if(i < 72):
            R[i+9] = 5
        if(i%9 != 0):
            R[i-1] = 5
        if(i%9 != 8):
            R[i+1] = 5
        M.append(R)

def create_car():
    speed = random.randint(2, 4)
    origin = rand_place()
    dest = rand_place()
    new_car = Car(speed, origin, dest)
    global M
    M = new_car.route(M)