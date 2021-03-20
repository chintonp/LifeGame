import tkinter as tk
import CellLG
#import LifeGameUI

class CellLGUI:

    def __init__(self, lgui, col, row, cell_col_len, cell_row_len, color):
        self.cell = lgui.lg.lifeMatrix[row][col]
        self.lgui = lgui
        self.cellgui = lgui.canvas.create_oval(col * cell_col_len + lgui.offset_x,
                                            row * cell_row_len + lgui.offset_y,
                                            (col + 1) * cell_col_len - 1 + lgui.offset_x,
                                            (row + 1) * cell_row_len -1 + lgui.offset_y,
                                            fill = color,
                                            outline = '')

        #                                         cy * cell_square_y + self.offset_y, 
        #                                         (cx + 1) * cell_square_x - 1 + self.offset_x, 
        #                                         (cy + 1) * cell_square_y -1 + self.offset_y, 
        #    
        # 
        #                                     fill = self.alive_color, outline='')))

    def updateCell(self, alive_color, dead_color):
        if self.cell.verifyChange():
            if self.cell.isCellAlive():
                self.fade(dead_color, alive_color, 0)
            else:
                self.fade(alive_color, dead_color, 0)


    def fade(self, origin_color, dest_color, step):    
        if (step == (self.lgui.fade_steps - 1)):
            self.lgui.canvas.itemconfig(self.cellgui, fill = dest_color)
        else:
            next_step = step + 1
            red_origin = int(origin_color[1:3],16)
            green_origin = int(origin_color[3:5],16)
            blue_origin = int(origin_color[5:],16)
            red_dest = int(dest_color[1:3],16)
            green_dest = int(dest_color[3:5],16)
            blue_dest = int(dest_color[5:],16)

            factor = next_step / self.lgui.fade_steps
            #print ("Factor: ", factor)
            red = int(red_origin + (red_dest - red_origin) * factor)
            #red = int((red_origin + red_destinarion) * factor)
            #print("Red: ", red)
            green = int(green_origin + (green_dest - green_origin) * factor)
            #green = int((green_origin + green_destinarion) * factor)
            #print("Green: ", green)
            blue = int(blue_origin + (blue_dest - blue_origin) * factor)
            #blue = int((blue_origin + blue_destinarion) * factor)
            #print ("Blue: ", blue)
            fade_color = "#" + str(hex(red))[2:] + str(hex(green))[2:] + str(hex(blue))[2:]
            #print ("Red: ", str(hex(red)), " - [2:]: ", str(hex(red))[2:] )
            #print ("Fade color = ", fade_color)
            self.lgui.canvas.itemconfig(self.cellgui, fill = fade_color)
            #print ("Next interval: ", int(self.lg.gen_interval / self.lg.fade_steps))
            self.lgui.canvas.after(int(self.lgui.gen_interval / self.lgui.fade_steps), self.fade, origin_color, dest_color, next_step)
