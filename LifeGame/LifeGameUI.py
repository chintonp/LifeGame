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
FADE_STEPS = 0
ALIVE_COLOR = "#0000FF"
DEAD_COLOR = "#FFFFFF"
NO_CANVAS = False

class LifeGameUI:

    def __init__(self, lifeGame, height = HEIGHT, width = WIDTH, title = TITLE, 
                life_rows = LIFE_ROWS, life_cols = LIFE_COLS, offset_x = OFFSET_X, 
                offset_y = OFFSET_Y, gen_interval = GEN_INTERVAL, fade_steps = FADE_STEPS,
                alive_color = ALIVE_COLOR, dead_color = DEAD_COLOR, no_canvas = NO_CANVAS):

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
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.no_canvas = no_canvas
        self.end_game = False


    def run(self):
        self.rootTk = tk.Tk()
        self.rootTk.title(self.title)
        frame = tk.Frame(self.rootTk)
        self.genLabel = tk.Label(frame, text="Generation: 0")
        self.genLabel.pack(pady = 5)
        self.btn = tk.Button(frame, text="Stop")
        self.btn.bind("<Button-1>", self.clickBtn)
        self.btn.pack(side = tk.LEFT)
        self.statBtn = tk.Button(frame, text="Stats", state=tk.DISABLED)
        self.statBtn.bind("<Button-1>", self.clickStatBtn)
        self.statBtn.pack(side = tk.RIGHT)
        frame.pack(pady = 10, padx = 75)
        self.isRunning = True
        self.lifeMatrixUI = []
        self.lg.max_gen -= 1
        if (self.no_canvas == False):
            self.canvas = tk.Canvas(self.rootTk, height= self.height + 2 * self.offset_y, width= self.width + 2 * self.offset_x, bg=self.dead_color)
            cell_square_x = self.width / self.life_cols
            cell_square_y = self.height / self.life_rows

            color = lambda x, y, lg: self.alive_color if lg.isCellAlive(x, y) else self.dead_color

            for cy in range(self.life_rows):
                row = []
                for cx in range(self.life_cols):
                    cell = self.createCellUI(cx, cy, cell_square_x, cell_square_y, color(cx, cy, self.lg))
                    row.append(cell)
                self.lifeMatrixUI.append(row)
         
            self.canvas.pack()
        
        self.genLabel.after(self.gen_interval, self.nextGen)
        self.rootTk.mainloop()


    def createCellUI(self, col, row, cell_row_len, cell_col_len, color):
        return clgui.CellLGUI(self, col, row, cell_row_len, cell_col_len, color)


    def nextGen(self):
        if (self.lg.genN < self.lg.max_gen):
            if self.lg.calcNextGen(self.no_canvas):
                if (self.no_canvas == False):
                    for y in range(self.life_rows):
                        for x in range(self.life_cols):
                            self.lifeMatrixUI[y][x].updateCell(self.alive_color, self.dead_color)
            else:
                self.stopRunning()
                self.end_game = True
        
            self.genLabel.config(text = 'Generation: ' + str(self.lg.genN))
        else:
            self.stopRunning()
        if self.isRunning:
            self.genLabel.after(self.gen_interval, self.nextGen)  


    def clickBtn(self, event):
        if self.isRunning:
            self.stopRunning()
        elif not self.end_game:
            self.btn.configure(text="Stop")
            self.statBtn['state'] = tk.DISABLED
            self.isRunning = True
            self.nextGen()

    
    def stopRunning(self):
        self.btn.configure(text="Start")
        self.statBtn['state'] = tk.NORMAL
        self.isRunning = False
    
    def clickStatBtn(self, event):
        if self.statBtn['state'] == tk.DISABLED:
            return
        
        report = self.lg.generateReport(self.lg.stats())

        newWindow = tk.Toplevel(self.rootTk)
        newWindow.title("Stats Report")
        label = tk.Label(newWindow, justify=tk.LEFT, padx = 10, pady = 10, font = "Verdana 10", text = report )
        label.pack()


