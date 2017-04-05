from .way import Way


class Thing:

    def __init__(self):
        self.path = []
        self.step = 0

    def moving(self, maze):
        try:
            maze.move(self.path[self.step].way)
        except IndexError:
            self.path.append(Step())


class Step:

    def __init__(self):
        self.way = Way.NONE
        self.not_tried = [Way.FRONT, Way.LEFT, Way.RIGHT]
