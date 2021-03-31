import random
import pandas as pd
import statistics as st

ALIVE = 1
DEAD = 0   
STATE = (ALIVE, DEAD) 

class CellLG:

    def __init__(self, x, y):
        self.id = (x, y)
        self.isBorn() 
        self.changed = False
        self.genBirth = 0
        self.info = { "id": self.id }
        self.genNumber = 0


    def isBorn(self):
        self.isAlive = random.choice(STATE)
        if self.isAlive:
            self.toLife(0)

    def isCellAlive(self):
        if self.isAlive == ALIVE:
            return True
        else:
            return False

    def calcNextGen(self, number_alive, genN, no_canvas):
        if self.isAlive == ALIVE:
            if number_alive > 3:
                self.toDead(genN)
        else:
            if number_alive >= 2 and number_alive <= 3:
                self.toLife(genN)
        changed = self.changed    
        if no_canvas:
            self.changed = False
        return changed
        

    def toDead(self, genN):
        self.isAlive = DEAD
        self.changed = True
        age = genN - self.genBirth
        self.info["Gen." +  str(self.genNumber)] = age
        self.genNumber += 1


    def toLife(self, genN):
        self.isAlive = ALIVE
        self.changed = True
        self.genBirth = genN


    def verifyChange(self):
        r = self.changed
        self.changed = False
        return r


    def endGame(self, genN):
        if self.isAlive == ALIVE:
            self.toDead(genN)


    # def calculateAge(self, genN):
    #     age = genN - self.genBirth
    #     self.info["Gen." +  str(self.genNumber)] = age
    #     self.genNumber += 1


    # def stats(self):
    #    series = pd.Series({ "id": self.id})
    #    return (series.append(pd.Series(self.info)))