import LifeGame as lg
import LifeGameUI as lgui
import numpy as np

TOLERANCE = 0.1
NUMBER_ITER_INIT = 1000

class LifeGameSim:

    def __init__ (self, life_cols = lgui.LIFE_COLS, life_rows = lgui.LIFE_ROWS, max_gen = lg.MAX_GENERATION, tolerance = TOLERANCE):
        self.life_cols = life_cols
        self.life_rows = life_rows
        self.max_gen = max_gen
        self.tolerance = tolerance

    def run(self, niter_init = NUMBER_ITER_INIT):
        running = True
        ni = niter_init
        while running:
            print ("Runnig sample 1 for ni = ", ni)
            dres1 = self.runSample(ni)
            print ("Runnig sample 2 for ni = ", ni)
            dres2 = self.runSample(ni)
            diff_mean_oldest = abs(dres1['mean_oldest'] - dres2['mean_oldest'])
            diff_std_oldest = abs(dres1['stdev_oldest'] - dres2['stdev_oldest'])
            if (diff_mean_oldest < dres1['mean_oldest'] * self.tolerance and diff_mean_oldest < dres2['mean_oldest'] * self.tolerance
                and  diff_std_oldest < dres1['stdev_oldest'] * self.tolerance and diff_std_oldest < dres2['stdev_oldest'] * self.tolerance):
                running = False
            else:
                ni *= 2

        dres1['n_iter'] = ni
        return dres1
    
    def runSample(self, ni):
        aoldest = np.zeros(ni)
        #aaveage = []
        #amaxgen = []
        for i in range(ni):
            #print ("Iteration: ", i)
            print (".", end='', flush=True)
            lgame = lg.LifeGame(life_cols = self.life_cols, life_rows = self.life_rows, max_gen = self.max_gen, no_gui = True, silent = True)
            dresults = lgame.run()
            aoldest[i] = dresults['oldest']
            #aaveage.append(dresults['ave_age'])
            #amaxgen.append(dresults['max_gen'])
        print("!", flush = True)
        #npaoldest = np.array(aoldest)
        dres = {}
        dres['mean_oldest'] = np.nanmean(aoldest)
        dres['stdev_oldest'] = np.nanstd(aoldest, ddof = 0)
        print ("Average oldest: ", dres['mean_oldest'])
        print ("Standard deviation: ", dres['stdev_oldest'])
        #print (npaoldest)
        #print (aaveage)
        #print (amaxgen)
        return dres

