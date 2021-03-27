import tkinter as tk
import CellLG as c
import LifeGameUI as lgui
import pandas as pd

NO_GUI = False
MAX_GENERATION = 100000
VERSION = "0.2.4"

class LifeGame:

    def __init__(self, height = lgui.HEIGHT, width = lgui.WIDTH, title = lgui.TITLE, 
                life_rows = lgui.LIFE_ROWS, life_cols = lgui.LIFE_COLS, offset_x = lgui.OFFSET_X, 
                offset_y = lgui.OFFSET_Y, gen_interval = lgui.GEN_INTERVAL, fade_steps = lgui.FADE_STEPS,
                alive_color = lgui.ALIVE_COLOR, dead_color = lgui.DEAD_COLOR, no_canvas = lgui.NO_CANVAS,
                no_gui = NO_GUI, max_gen = MAX_GENERATION):
        
        self.rows = life_rows
        self.cols = life_cols
        self.no_gui = no_gui
        self.max_gen = max_gen
        self.genN = 0
        title = title + " - (" + str(life_rows) + " x " + str(life_cols) + ")"
        self.lifeMatrix = []

        for y in range(self.cols):
            row = []
            for x in range(self.rows):
                row.append(c.CellLG(x, y))
            self.lifeMatrix.append(row)

        if no_gui:
            self.initNoGui(title)
        else:
            self.lgu = lgui.LifeGameUI(self, height, width, title, self.rows, self.cols, offset_x, 
                offset_y, gen_interval, fade_steps, alive_color, dead_color, no_canvas)

                    
    def initNoGui(self, title):
        print("\n***** Game of Life *****")
        print("Version: ", VERSION)
        print(title)
        print("")

    
    def run(self):
        if (self.no_gui):
            self.runGame()
        else:
            self.lgu.run()

    def runGame(self):
        changed = True
        while (changed == True and self.genN < self.max_gen):
            print("Generation: ", self.genN, end = '\r')
            changed = self.calcNextGen()
        print('\n')
        self.stats()

    
    def isCellAlive(self, x, y):
        return self.lifeMatrix[y][x].isCellAlive()


    def neighborCount(self):
        neighborLifeMatrix = []
        for cy in range(self.rows):
            row = []
            for cx in range(self.cols):
                x_init = cx - 1
                x_end = cx + 1
                y_init = cy - 1
                y_end = cy + 1
                if cx == 0:
                    x_init = 0
                elif cx == self.cols - 1:
                    x_end = cx
                if   cy == 0:
                    y_init = 0
                elif cy == self.rows - 1:
                    y_end = cy 
                number_alive = 0
                for y in range (y_init, y_end + 1):
                    for x in range (x_init, x_end + 1):
                        if self.lifeMatrix[y][x].isCellAlive() :
                            number_alive += 1 
                        #print ("x: ", x, " - y: ", y, " - number_alive: ", number_alive)
                row.append(number_alive)
            neighborLifeMatrix.append(row)
        return neighborLifeMatrix


    def calcNextGen(self):
        self.genN += 1
        changed = False
        neighborMatrix = self.neighborCount()
        for y in range(self.rows):
            for x in range(self.cols):
                if self.lifeMatrix[y][x].calcNextGen(neighborMatrix[y][x], self.genN, self.no_gui):
                    changed = True
        return changed


    def stats(self):
        columns = ['id', 'avg', 'stdev']
        columns_size = columns.len()
        df = pd.DataFrame(columns = columns)    
        for y in range(self.rows):
            for x in range(self.cols):
                print(".", end='', flush = True)
                #pd.append(self.lifeMatrix[y][x].stats())
                df = df.append(self.lifeMatrix[y][x].stats(), ignore_index = True)
            print(y, end = '', flush = True)
        print("!", flush = True)
        df['avg'] = df.iloc[: , columns_size:].mean(axis = 1)
        df['stdev'] = df.iloc[: , columns_size:].std(ddof = 0, axis = 1)
        print (df)