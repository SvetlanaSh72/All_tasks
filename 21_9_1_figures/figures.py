class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    #count perimetr
    def get_perim_rect(self):
        return 2*(self.height+self.width)

class Сircle:
    def __init__(self, radius=0):
        self.radius = radius
    # count L Сircle
    def get_circle_l(self):
        #pi=3.14
        return 2*3.14*(self.radius)
