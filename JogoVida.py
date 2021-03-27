import LifeGame as lg

#jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=10, life_cols = 10, gen_interval = 50, dead_color = "#BB88BB", alive_color = "#4400CC", max_gen = 100, no_canvas = True)
jogo = lg.LifeGame(life_rows=15, life_cols = 15, no_gui = True)
jogo.run()