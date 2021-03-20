import tkinter as tk
import CellLGUI as clgui


HEIGHT = 600
WIDTH = 800
TITLE = "Game of Life"
LIFE_ROWS = 30
LIFE_COLS = 30
OFFSET_X = 5
OFFSET_Y = 5
GEN_INTERVAL = 1000 #miliseconds
FADE_STEPS = 3
ALIVE_COLOR = "#0000FF"
DEAD_COLOR = "#FFFFFF"

class LifeGameUI:

    def __init__(self, lifeGame, height = HEIGHT, width = WIDTH, title = TITLE, 
                life_rows = LIFE_ROWS, life_cols = LIFE_COLS, offset_x = OFFSET_X, 
                offset_y = OFFSET_Y, gen_interval = GEN_INTERVAL, fade_steps = FADE_STEPS,
                alive_color = ALIVE_COLOR, dead_color = DEAD_COLOR):

        self.lg = lifeGame
        self.height = height
        self.width = width
        self.title = title
        self.life_rows = life_rows
        self.life_cols = life_cols
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.gen_interval = gen_interval
        self.fade_steps = fade_steps
        self.alive_color = ALIVE_COLOR
        self.dead_color = DEAD_COLOR

    def run(self):
        root = tk.Tk()
        root.title(self.title)
        self.genLabel = tk.Label(text="Generation: 0")
        self.genLabel.pack()
        self.btn = tk.Button(text="Stop")
        self.btn.bind("<Button-1>", self.clickBtn)
        self.btn.pack()
        self.isRunning = True
        self.canvas = tk.Canvas(root, height= self.height + 2 * self.offset_y, width= self.width + 2 * self.offset_x, bg=self.dead_color)
        cell_square_x = self.width / self.life_cols
        cell_square_y = self.height / self.life_rows

        self.lifeMatrixUI = []
        color = lambda x, y, lg: self.alive_color if lg.isCellAlive(x, y) else self.dead_color

        for cy in range(self.life_rows):
            row = []
            for cx in range(self.life_cols):
                #cell = self.createCellUI(self.lg.lifeMatrix[cy][cy], self.canvas, cx, cy, cell_square_x, cell_square_y, self.offset_x, self.offset_y, color(cx, cy, self.lg))
                cell = self.createCellUI(cx, cy, cell_square_x, cell_square_y, color(cx, cy, self.lg))
                row.append(cell)
            self.lifeMatrixUI.append(row)

        self.genN = 0
        
        self.canvas.pack()
        self.canvas.after(self.gen_interval, self.nextGen)
        root.mainloop()


    def createCellUI(self, col, row, cell_row_len, cell_col_len, color):
        return clgui.CellLGUI(self, col, row, cell_row_len, cell_col_len, color)


    def nextGen(self):
        self.genN += 1
        self.genLabel.config(text = 'Generation: ' + str(self.genN))

        self.lg.calcNextGen()

        for y in range(self.life_rows):
            for x in range(self.life_cols):
                self.lifeMatrixUI[y][x].updateCell(self.alive_color, self.dead_color)
        

        if self.isRunning:
            self.canvas.after(self.gen_interval, self.nextGen)  


    def clickBtn(self, event):
        if self.isRunning:
            self.btn.configure(text="Start")
            self.isRunning = False
        else:
            self.btn.configure(text="Stop")
            self.isRunning = True
            self.nextGen()