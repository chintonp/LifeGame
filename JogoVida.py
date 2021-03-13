import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 20", life_rows=40, life_cols = 40, gen_interval = 500, fade_steps = 5)
jogo.run()