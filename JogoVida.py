import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 50", life_rows=10, life_cols = 10, gen_interval = 250, dead_color = "#BB88BB", alive_color = "#4400CC")
jogo.run()