import LifeGame as lg

jogo = lg.LifeGame(title="Jogo da Vida 100", life_rows=100, life_cols = 100, gen_interval = 500, fade_steps = 0)
jogo.run()