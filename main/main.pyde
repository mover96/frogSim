class Frog:
    radius = 20
    frogColor = color(13, 158, 32)
    direction = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lastX = x
        self.lastY = y
        
    def _d(self):
        fill(self.frogColor)
        circle(self.x, self.y, self.radius * 2)

    def tick(self):
        if (not self.is_valid_move(mouseX, mouseY, self.radius)):
            self.x = self.lastX
            self.y = self.lastY
        else:
            self.x = mouseX
            self.y = mouseY
            self.lastX = self.x
            self.lastY = self.y
        self._d()
    
    @staticmethod
    def is_valid_move(x, y, frogRadius):
        if (x + frogRadius >= width or y + frogRadius >= height
                or x - frogRadius <= 0 or y - frogRadius <= 0):
            return False
        return True

def setup():
    size(400,400)
    frameRate(60)

f = Frog(200,50)
def draw():
    background(color(3, 169, 252))
    f.tick()
    
