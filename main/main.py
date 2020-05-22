import math

class Frog:
    body_width = 20
    body_height = 20
    head_width = 10
    head_height = 10
    frogColor = color(13, 158, 32)
    direction = 1

    def __init__(self, w, h):
        self.w = w
        self.h = h

        spawn = self.get_spawn()
        self.x = spawn[0]
        self.y = spawn[1]
        self.theta = spawn[2]
        
    def _d(self):
        self._draw_body()
        self._draw_head()

    def _draw_body(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.theta)
        fill(self.frogColor)
        rect(0, 0, self.body_width, self.body_height)
        popMatrix()

    def _draw_head(self):
        mid = (self.body_width / 2) - self.head_width
        hCenter = (-self.head_height * 2) * 0.6
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.theta)
        rectMode(CENTER)
        fill(self.frogColor)
        rect(mid, hCenter, self.head_width, self.head_height)
        popMatrix()


    def _make_move(self):
        r = random(-1,1)
        x_dir = (-1, 1)[r  < 0]
        r = random(-1,1)
        y_dir = (-1, 1)[r  < 0]

        x_pon = self.x + x_dir
        y_pon = self.y + y_dir

        if (self.is_valid_move(x_pon, y_pon)):
            self.x = x_pon
            self.y = y_pon

    def tick(self):
        self._make_move()
        self._d()
    
    def is_valid_move(self, x, y):
        if (x + self.body_width >= self.w or y + self.body_height >= self.h
                or x <= 0 or y <= 0):
            return False
        return True

    def get_spawn(self):
        x = self._randint(self.body_width + 1, self.w - self.body_width - 1)
        y = self._randint(self.body_height + 1, self.h - self.body_height - 1)
        theta = random(0, 2 * PI)
        return (x,y, theta)

    @staticmethod
    def _randint(low, high):
        return math.ceil(random(low, high))

def setup():
    size(400,400)
    frameRate(60)
    global frogs
    frogs = []
    for _ in range(10):
        frogs.append(Frog(width, height))


def draw():
    background(color(3, 169, 252))
    for f in frogs:
        f.tick()
    