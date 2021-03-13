import tkinter as tk
import random

ALIVE = 1
DEAD = 0   
STATE = (ALIVE, DEAD) 

class CellLG:

    def __init__(self, canvas, cell_gr):
        self.isAlive = random.choice(STATE) 
        self.canvas = canvas
        self.cell_gr = cell_gr
        color = 'blue'
        if self.isAlive == DEAD:
            canvas.itemconfig(self.cell_gr, fill = 'white')


    def lifeCalc(self, number_alive):
        if self.isAlive == ALIVE:
            if number_alive > 3:
                self.toDead()
        else:
            if number_alive >= 2 and number_alive <= 3:
                self.toLife()    
        

    def toDead(self):
        self.isAlive = DEAD
        self.canvas.itemconfig(self.cell_gr, fill = 'white')


    def toLife(self):
        self.isAlive = ALIVE
        self.canvas.itemconfig(self.cell_gr, fill = 'blue')