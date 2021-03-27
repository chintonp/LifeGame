import tkinter as tk
import CellLG as c
import LifeGameUI as lgui
import pandas as pd

COLUMN_STAT = 3

class LifeGame:

    def __init__(self, height = lgui.HEIGHT, width = lgui.WIDTH, title = lgui.TITLE, 
                life_rows = lgui.LIFE_ROWS, life_cols = lgui.LIFE_COLS, offset_x = lgui.OFFSET_X, 
                offset_y = lgui.OFFSET_Y, gen_interval = lgui.GEN_INTERVAL, fade_steps = lgui.FADE_STEPS,
                alive_color = lgui.ALIVE_COLOR, dead_color = lgui.DEAD_COLOR, no_canvas = lgui.NO_CANVAS):
        
        self.rows = life_rows
        self.cols = life_cols

        self.lifeMatrix = []

        for y in range(self.cols):
            row = []
            for x in range(self.rows):
                row.append(c.CellLG(x, y))
            self.lifeMatrix.append(row)

        self.lgu = lgui.LifeGameUI(self, height, width, title, self.rows, self.cols, offset_x, 
                offset_y, gen_interval, fade_steps, alive_color, dead_color, no_canvas)

                    
    def run(self):
        self.lgu.run()

    
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
        changed = False
        neighborMatrix = self.neighborCount()
        for y in range(self.rows):
            for x in range(self.cols):
                if self.lifeMatrix[y][x].calcNextGen(neighborMatrix[y][x], self.lgu.genN):
                    changed = True
        return changed


    def stats(self):
        df = pd.DataFrame(columns = ['id', 'avg', 'stdev'])    
        for y in range(self.rows):
            for x in range(self.cols):
                #pd.append(self.lifeMatrix[y][x].stats())
                df = df.append(self.lifeMatrix[y][x].stats(), ignore_index = True)
        df['avg'] = df.iloc[: , COLUMN_STAT:].mean(axis = 1)
        df['stdev'] = df.iloc[: , COLUMN_STAT:].std(ddof = 0, axis = 1)
        print (df)