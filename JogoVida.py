import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=50, life_cols = 50, gen_interval = 200, no_canvas = True)
jogo.run()