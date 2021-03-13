import tkinter as tk
from tkinter.constants import TRUE
import CellLG as c


HEIGHT = 600
WIDTH = 800
TITLE = "Game of Life"
LIFE_ROWS = 30
LIFE_COLS = 30
OFFSET_X = 5
OFFSET_Y = 5
GEN_INTERVAL = 1000 #miliseconds

class LifeGame:

    def __init__(self, height = HEIGHT, width = WIDTH, title = TITLE, 
                life_rows = LIFE_ROWS, life_cols = LIFE_COLS, offset_x = OFFSET_X, 
                offset_y = OFFSET_Y, gen_interval = GEN_INTERVAL):
        
        self.height = height
        self.width = width
        self.title = title
        self.life_rows = life_rows
        self.life_cols = life_cols
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.gen_interval = gen_interval


    def run(self):
        root = tk.Tk()
        root.title(self.title)
        self.genLabel = tk.Label(text="Generation: 0")
        self.genLabel.pack()
        self.btn = tk.Button(text="Stop")
        self.btn.bind("<Button-1>", self.clickBtn)
        self.btn.pack()
        self.isRunning = True
        self.canvas = tk.Canvas(root, height= self.height + 2 * self.offset_y, width= self.width + 2 * self.offset_x, bg='white')
        cell_square_x = self.width / self.life_cols
        cell_square_y = self.height / self.life_rows

        self.lifeMatrix = []

        for cy in range(self.life_rows):
            row = []
            for cx in range(self.life_cols):
                cell = c.CellLG(self.canvas, self.canvas.create_oval(cx * cell_square_x + self.offset_x, 
                                                cy * cell_square_y + self.offset_y, 
                                                (cx + 1) * cell_square_x - 1 + self.offset_x, 
                                                (cy + 1) * cell_square_y -1 + self.offset_y, 
                                                fill = 'blue', outline=''))
                row.append(cell)
            self.lifeMatrix.append(row)

        self.genN = 0
        
        self.canvas.pack()
        self.canvas.after(self.gen_interval, self.nextGen)
        root.mainloop()


    def nextGen(self):
        self.genN += 1
        self.genLabel.config(text = 'Generation: ' + str(self.genN))
        #print("Generation: ", self.genN)
        neighborLifeMatrix = []
        for cy in range(self.life_rows):
            row = []
            for cx in range(self.life_cols):
                x_init = cx - 1
                x_end = cx + 1
                y_init = cy - 1
                y_end = cy + 1
                if cx == 0:
                    x_init = 0
                elif cx == self.life_cols - 1:
                    x_end = cx
                if   cy == 0:
                    y_init = 0
                elif cy == self.life_rows - 1:
                    y_end = cy 
                
                #print ("x_init: " + str(x_init) + " - x_end: " + str(x_end) + " - y_init: " + str(y_init) + " - y_end: " + str(y_end))
                number_alive = 0
                for y in range (y_init, y_end + 1):
                    for x in range (x_init, x_end + 1):
                        #print ("x: ", x, " - y: ", y)
                        if self.lifeMatrix[y][x].isAlive == c.ALIVE:
                            number_alive += 1        
                row.append(number_alive)
            neighborLifeMatrix.append(row)

        for cy in range(self.life_rows):
            for cx in range(self.life_rows):
                self.lifeMatrix[cy][cx].lifeCalc(neighborLifeMatrix[cy][cx])     
        
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
