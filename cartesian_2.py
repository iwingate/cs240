import math

class Point(object);
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
    
    def distance (self, x_param = 0.0, y_param = 0.0):
        x_diff = self.x - param_pt.x
        y_diff = self.y - param_pt.y
        return math.sqrt(x_diff**2 + y_diff**2)
   
    def sum (self, param_pt):
        new_pt = Point()
        new_pt.x = self.x + param_pt.x
        new_pt.y = self.y + param_pt.y
        return new_pt

    def __str__(self): 
        print('called the __str__ method')
        return '({:.2f}, {:.2f}'.format(self.x,self.y)
