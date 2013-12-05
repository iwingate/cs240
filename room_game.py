import random

class rooms(object):

    def __init__(self,z):
        self.grid_size = z
        self.grid = []
        for i in range(z):
            row = [0] * z
            self.grid.append(row)

    def __str__(self):
        s = ''
        for j in range(self.grid_size):
            for i in range(self.grid_size):
                if not self.grid[i][j]:
                    s += '{}'.format(' _ ')
                else:
                    s += '{}'.format(str(self.grid[i][j]))
            s += '\n'
        return s

    def register(self, person):
        x = person.x
        y = person.y
        self.grid[x][y] = person

class Person(object):
    def __init__(self,x=0,y=0,name=' p1 '):
        self.x = x
        self.y = y
        self.name = name
 
    def __str__(self):
        return self.name
