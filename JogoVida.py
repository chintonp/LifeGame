import LifeGame.LifeGame as lg

#jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=5, life_cols = 10, gen_interval = 50, dead_color = "#BB88BB", alive_color = "#4400CC", max_gen = 100)
jogo = lg.LifeGame(life_rows = 5, life_cols = 5, gen_interval = 200, no_canvas=False)
jogo.run()