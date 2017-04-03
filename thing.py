import math

def length(x, y, a, b):
    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

class Thing:
    def __init__(self, x, y, keys):
        self.x = x
        self.y = y
        self.keys = keys

    def use(self, key, map):
        map.use_key(key)
        self.x = map.thing[0]
        self.y = map.thing[1]

    def conclude(self, key, init_x, init_y, map):
        if (init_x, init_y) == (self.x, self.y):
            key.value = -1
        else:
            if (length(init_x, init_y, self.x, self.y)) > length(init_x, init_y, self.x, self.y):
                key.value = 2
            else:
                key.value = 1