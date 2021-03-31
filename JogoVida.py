import LifeGame.LifeGameSim as lgs

#jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=5, life_cols = 10, gen_interval = 50, dead_color = "#BB88BB", alive_color = "#4400CC", max_gen = 100)
#jogo = lg.LifeGame(life_rows = 5, life_cols = 5, gen_interval = 200, no_canvas=True)
#jogo.run()

rows = 10
cols = 10
max_gen = 1000
tolerance = 0.05

sim = lgs.LifeGameSim(life_cols = cols, life_rows = rows, max_gen = max_gen, tolerance = tolerance)
dresults = sim.run()

print("***** Game of Life *****")
print("Rows: ", rows, " - Cols: ", cols)
print("Max number of generations: ", max_gen)
print("Tolerance: ", tolerance)
print("\nResults:")
print("- Number of iterations", 2 * dresults['n_iter'])
print("- Averade oldest: ", dresults['mean_oldest'], " +/- ", tolerance * 100, "%")
print("- Averade std dev: ", dresults['stdev_oldest'], " +/- ", tolerance * 100, "%")