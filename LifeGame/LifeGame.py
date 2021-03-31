import tkinter as tk
import LifeGame.CellLG as c
import LifeGame.LifeGameUI as lgui
import pandas as pd
import numpy as np

NO_GUI = False
MAX_GENERATION = 100000
VERSION = "0.3.0.1"
SILENT = False

class LifeGame:

    def __init__(self, height = lgui.HEIGHT, width = lgui.WIDTH, title = lgui.TITLE, 
                life_rows = lgui.LIFE_ROWS, life_cols = lgui.LIFE_COLS, offset_x = lgui.OFFSET_X, 
                offset_y = lgui.OFFSET_Y, gen_interval = lgui.GEN_INTERVAL, fade_steps = lgui.FADE_STEPS,
                alive_color = lgui.ALIVE_COLOR, dead_color = lgui.DEAD_COLOR, no_canvas = lgui.NO_CANVAS,
                no_gui = NO_GUI, max_gen = MAX_GENERATION, silent = SILENT):
        
        self.rows = life_rows
        self.cols = life_cols
        self.no_gui = no_gui
        if no_gui:
            no_canvas = True
        self.max_gen = max_gen
        self.silent = silent
        self.genN = 0
        title = title + " - (" + str(life_rows) + " x " + str(life_cols) + ")"
        self.lifeMatrix = []

        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                row.append(c.CellLG(x, y))
            self.lifeMatrix.append(row)

        if no_gui and not self.silent:
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
            return self.runGame()
        else:
            self.lgu.run()

    def runGame(self):
        changed = True
        while (changed == True and self.genN < self.max_gen):
            if not self.silent:
                print("Generation: ", self.genN, end = '\r')
            changed = self.calcNextGen()
        if not self.silent:
            print('\n')
        dresults = self.stats()
        if self.no_gui and not self.silent:
            print(self.generateReport(dresults))
        return dresults

    
    def isCellAlive(self, x, y):
        #print ("x - ", x, " : ", " y - ", y)
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


    def calcNextGen(self, no_canvas = True):
        self.genN += 1
        changed = False
        neighborMatrix = self.neighborCount()
        for y in range(self.rows):
            for x in range(self.cols):
                if self.lifeMatrix[y][x].calcNextGen(neighborMatrix[y][x], self.genN, no_canvas):
                    changed = True
        return changed


    def stats(self):
        for y in range(self.rows):
            for x in range(self.cols):
                self.lifeMatrix[y][x].endGame(self.genN)


        #columns = ['avg', 'stdev', 'numGen', 'maxAge']
        columns = [ 'numGen' ]
        gen_info_start = len(columns) + 1
        #df = pd.DataFrame(columns = columns)    
        data = []
        for y in range(self.rows):
            for x in range(self.cols):
                #print(".", end='', flush = True)
                #pd.append(self.lifeMatrix[y][x].stats())
                #df = df.append(self.lifeMatrix[y][x].info, ignore_index = True)
                data.append(self.lifeMatrix[y][x].info)
            #print(y, end = '', flush = True)
        #print("!\n", flush = True)
        
        i = 0
        d = {}
        for entry in data:
            d[i] = entry
            i += 1
        df= pd.DataFrame.from_dict(d, "index")
        
        i = 1
        for col in columns:
            #print (col, flush=True)
            df.insert(i, col, 0)
            i += 1

        #df['avg'] = df.iloc[: , gen_info_start:].mean(axis = 1)
        #df['stdev'] = df.iloc[: , gen_info_start:].std(ddof = 0, axis = 1)
        df['numGen'] = df.iloc[: , gen_info_start:].count(axis = 1)
        #df['maxAge'] = df.iloc[: , gen_info_start:].max(axis = 1)
        
        #print(df)

        values = df.iloc[: , gen_info_start:].values
        #print (values)

        dresults = {}

        dresults ['num_it'] = self.genN
        dresults ['oldest'] = np.nanmax(values)
        dresults ['ave_age'] = np.nanmean(values)
        dresults ['std_age'] = np.nanstd(values)
        dresults ['max_gen'] = df['numGen'].max()
        dresults ['min_gen'] = df['numGen'].min()
        dresults ['ave_gen'] = df['numGen'].mean()
        dresults ['std_gen'] = df['numGen'].std(ddof = 0)

        # report = "***** Game of Life Report *****\n"
        # report = report + "- Number of iterations: " + str(self.genN)
        # report = report + "\n- Oldest cell: " + str (np.nanmax(values))
        # report = report + "\n- Averade age: " + str (np.nanmean(values))
        # report = report + "\n- Standard deviation age: " + str(np.nanstd(values))
        # report = report + "\n- Max number of generations: " + str(df['numGen'].max())
        # report = report + "\n- Min number of genereations: " + str(df['numGen'].min())
        # report = report + "\n- Mean number of generations: " + str(df['numGen'].mean())
        # report = report + "\n- Standar deviation number of generations: " + str(df['numGen'].std(ddof = 0))
        
        #print (df.iloc[: , gen_info_start:])

        # if self.no_gui:
        #     print (report)

        return dresults

    def generateReport(self, dresults):
        report = "***** Game of Life Report *****\n"
        report = report + "- Number of iterations: " + str(dresults ['num_it'])
        report = report + "\n- Oldest cell: " + str (dresults ['oldest'])
        report = report + "\n- Averade age: " + str (dresults ['ave_age'])
        report = report + "\n- Standard deviation age: " + str(dresults ['std_age'])
        report = report + "\n- Max number of generations: " + str(dresults ['max_gen'])
        report = report + "\n- Min number of genereations: " + str(dresults ['min_gen'])
        report = report + "\n- Mean number of generations: " + str(dresults ['ave_gen'])
        report = report + "\n- Standard deviation number of generations: " + str(dresults ['std_gen'])
        return report

       
