import LifeGame
import tkinter as tk
import random

ALIVE = 1
DEAD = 0   
STATE = (ALIVE, DEAD) 

class CellLG:

    def __init__(self, lg, cell_gr):
        self.isAlive = random.choice(STATE) 
        self.lg = lg
        self.cell_gr = cell_gr
        self.fade_step_number = 0
        if self.isAlive == DEAD:
            self.lg.canvas.itemconfig(self.cell_gr, fill = lg.dead_color)


    def lifeCalc(self, number_alive):
        if self.isAlive == ALIVE:
            if number_alive > 3:
                self.toDead()
        else:
            if number_alive >= 2 and number_alive <= 3:
                self.toLife()    
        

    def toDead(self):
        self.isAlive = DEAD
        self.fade(self.lg.alive_color, self.lg.dead_color, 0)
        #print ("Aqui")


    def toLife(self):
        self.isAlive = ALIVE
        self.fade(self.lg.dead_color, self.lg.alive_color, 0)
        

    def fade(self, origin_color, destination_color, step):
        #print ("Step: ", step, " - Origin color: ", origin_color, " - Dest color: ", destination_color)
        if (step == (self.lg.fade_steps - 1)):
            self.lg.canvas.itemconfig(self.cell_gr, fill = destination_color)
        else:
            next_step = step + 1
            red_origin = int(origin_color[1:3],16)
            green_origin = int(origin_color[3:5],16)
            blue_origin = int(origin_color[5:],16)
            red_dest = int(destination_color[1:3],16)
            green_dest = int(destination_color[3:5],16)
            blue_dest = int(destination_color[5:],16)

            factor = next_step / self.lg.fade_steps
            #print ("Factor: ", factor)
            red = int(red_origin + (red_dest - red_origin) * factor)
            #red = int((red_origin + red_destinarion) * factor)
            #print("Red: ", red)
            green = int(green_origin + (green_dest - green_origin) * factor)
            #green = int((green_origin + green_destinarion) * factor)
            #print("Green: ", green)
            blue = int(blue_origin + (blue_dest - blue_origin) * factor)
            #blue = int((blue_origin + blue_destinarion) * factor)
            #print ("Blue: ", blue)
            fade_color = "#" + str(hex(red))[2:] + str(hex(green))[2:] + str(hex(blue))[2:]
            #print ("Red: ", str(hex(red)), " - [2:]: ", str(hex(red))[2:] )
            #print ("Fade color = ", fade_color)
            self.lg.canvas.itemconfig(self.cell_gr, fill = fade_color)
            #print ("Next interval: ", int(self.lg.gen_interval / self.lg.fade_steps))
            self.lg.canvas.after(int(self.lg.gen_interval / self.lg.fade_steps), self.fade, origin_color, destination_color, next_step)
