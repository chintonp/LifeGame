import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=50, life_cols = 50, gen_interval = 100, dead_color = "#BB88BB", alive_color = "#4400CC", fade_steps = 0, no_canvas = False)
jogo.run()