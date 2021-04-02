from LifeGame import VERSION
import LifeGameSim as lgs
import argparse


class LifeGameInit():

    def __init__(self):
        
        self.rows = 10
        self.cols = 10
        self.max_gen = 1000
        self.tolerance = 0.05
        self.niter_init = 750


        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--version", help="show program version", action="store_true")
        parser.add_argument("-r", "--rows", help="set number of rows")
        parser.add_argument("-c", "--cols", help="set number of columns")
        parser.add_argument("-m", "--maxgen", help="set maximal number of generatios")
        parser.add_argument("-t", "--tolerance", help="set error tolerance")
        parser.add_argument("-n", "--ninit", help="set initial number of iterations")
        args = parser.parse_args()

        if args.version:
            print ("Game of Live - version ", VERSION)
        if args.rows:
            self.rows = int(args.rows)
        if args.cols:
            self.cols = int(args.cols)
        if args.maxgen:
            self.max_gen = int(args.maxgen)
        if args.tolerance:
            self.tolerance = float(args.tolerance)
        if args.ninit:
            self.niter_init = int(args.init)

        print ("Game of Life - (" + str(self.cols) + " , " + str(self.rows) + ")")
        print ("Version: ", VERSION)
        print ("Parameters:")
        print ("- Max gen: ", self.max_gen)
        print ("- Tolerance: ", self.tolerance)
        print ("- Number initial iteraions: ", self.niter_init)
        print ("")

    
    def run(self):
        
        sim = lgs.LifeGameSim(life_cols = self.cols, life_rows = self.rows, max_gen = self.max_gen, tolerance = self.tolerance)
        dresults = sim.run(self.niter_init)


        print("\n***** Game of Life *****")
        print("Rows: ", self.rows, " - Cols: ", self.cols)
        print("Max number of generations: ", self.max_gen)
        print("Tolerance: ", self.tolerance)
        print("\nResults:")
        print("- Number of iterations", 2 * dresults['n_iter'])
        print("- Averade oldest: ", dresults['mean_oldest'], " +/- ", self.tolerance * 100, "%")
        print("- Averade std dev: ", dresults['stdev_oldest'], " +/- ", self.tolerance * 100, "%")
        
        
        

        


#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

#jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=5, life_cols = 10, gen_interval = 50, dead_color = "#BB88BB", alive_color = "#4400CC", max_gen = 100)
#jogo = lg.LifeGame(life_rows = 5, life_cols = 5, gen_interval = 200, no_canvas=True)
#jogo.run()

# rows = 10
# cols = 10
# max_gen = 1000
# tolerance = 0.05
# niter_init = 750

# sim = lgs.LifeGameSim(life_cols = cols, life_rows = rows, max_gen = max_gen, tolerance = tolerance)
# dresults = sim.run(niter_init)

# print("***** Game of Life *****")
# print("Rows: ", rows, " - Cols: ", cols)
# print("Max number of generations: ", max_gen)
# print("Tolerance: ", tolerance)
# print("\nResults:")
# print("- Number of iterations", 2 * dresults['n_iter'])
# print("- Averade oldest: ", dresults['mean_oldest'], " +/- ", tolerance * 100, "%")
# print("- Averade std dev: ", dresults['stdev_oldest'], " +/- ", tolerance * 100, "%")

if __name__ == '__main__':
    lgi = LifeGameInit()
    lgi.run()