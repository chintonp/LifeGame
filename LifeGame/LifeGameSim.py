import LifeGame.LifeGame as lg
import LifeGame.LifeGameUI as lgui
import numpy as np


class LifeGameSim:

    def __init__ (self, life_cols = lgui.LIFE_COLS, life_rows = lgui.LIFE_ROWS, max_gen = lg.MAX_GENERATION):
        self.life_cols = life_cols
        self.life_rows = life_rows
        self.max_gen = max_gen

    
    def run(self):
        aoldest = []
        aaveage = []
        amaxgen = []
        for i in range(10000):
            #print ("Iteration: ", i)
            lgame = lg.LifeGame(life_cols = self.life_cols, life_rows = self.life_rows, max_gen = self.max_gen, no_gui = True, silent = True)
            dresults = lgame.run()
            #report = lgame.generateReport(dresults)
            aoldest.append(dresults['oldest'])
            aaveage.append(dresults['ave_age'])
            amaxgen.append(dresults['max_gen'])
            #print (report)
            #print ("*****\n\n")

        npaoldest = np.array(aoldest)
        mean_oldest = np.nanmean(npaoldest)
        stdev_oldest = np.nanstd(npaoldest, ddof = 0)
        print ("Average oldest: ", mean_oldest)
        print ("Standard deviation: ", stdev_oldest)
        #print (npaoldest)
        #print (aaveage)
        #print (amaxgen)

