import random

ALIVE = 1
DEAD = 0   
STATE = (ALIVE, DEAD) 

class CellLG:

    def __init__(self, x, y):
        self.id = (x, y)
        self.isBorn() 
        self.changed = False
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

    def calcNextGen(self, number_alive):
        if self.isAlive == ALIVE:
            if number_alive > 3:
                self.toDead()
        else:
            if number_alive >= 2 and number_alive <= 3:
                self.toLife()    
        

    def toDead(self):
        self.isAlive = DEAD
        self.changed = True
    #    self.fade(self.lg.alive_color, self.lg.dead_color, 0)
        #print ("Aqui")


    def toLife(self):
        self.isAlive = ALIVE
        self.changed = True
    #    self.fade(self.lg.dead_color, self.lg.alive_color, 0)

    def verifyChange(self):
        r = self.changed
        self.changed = False
        return r