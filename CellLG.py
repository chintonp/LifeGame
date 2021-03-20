import random

ALIVE = 1
DEAD = 0   
STATE = (ALIVE, DEAD) 

class CellLG:

    def __init__(self, x, y):
        self.id = (x, y)
        self.isBorn() 
        self.changed = False
        self.genBirth = 0
        self.ages = []
        # self.lg = lg
        # self.cell_gr = cell_gr
        # self.fade_step_number = 0
        # if self.isAlive == DEAD:
        #     self.lg.canvas.itemconfig(self.cell_gr, fill = lg.dead_color)


    def isBorn(self):
        self.isAlive = random.choice(STATE)

    def isCellAlive(self):
        if self.isAlive == ALIVE:
            return True
        else:
            return False

    def calcNextGen(self, number_alive, genN):
        if self.isAlive == ALIVE:
            if number_alive > 3:
                self.toDead(genN)
        else:
            if number_alive >= 2 and number_alive <= 3:
                self.toLife(genN)    
        

    def toDead(self, genN):
        self.isAlive = DEAD
        self.changed = True
        age = genN - self.genBirth
        self.ages.append(age)


    def toLife(self, genN):
        self.isAlive = ALIVE
        self.changed = True
        self.genBirth = genN


    def verifyChange(self):
        r = self.changed
        self.changed = False
        return r