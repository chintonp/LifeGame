import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 3", life_rows=4, life_cols = 4, gen_interval = 5000, fade_steps = 8)
jogo.run()