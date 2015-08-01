__author__ = 'Steve'
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

SIDE = 50
MARGIN = 20 # pixels around the board
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

#  Create class to represent the UI inherited from Frame imported from Tkinter


class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for displaying the UI.
    """
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

        def __initUI(self):
            self.parent.title("Sudoku")
            self.pack(fill=BOTH, expand=1)  # Use all available space
            self.canvas = Canvas(self, width=WIDTH, heigh=HEIGHT)
            self.canvas.pack(fill=BOTH, side=TOP)  # Pull board to top of frame
            clear_button = Button(self, text="Clear answers", command=self.__clear_answers)
            clear_button.pack(fill=BOTH, side=BOTTOM)

            self.__draw_grid()
            self.__draw_puzzle()

            self.canvas.bind("<Button-1>", self.__cell_clicked)
            self.canvas.bind("<Key>", self.__key_pressed)

        def __draw_grid(self):
            """
            Draws grid divided with blue lines into 3 x 3 grid
            :return:
            """
            for i in range(10):
                color = 'blue' if i % 3 == 0 else "gray"

                x0 = MARGIN + i * SIDE
                y0 = MARGIN
                x1 = MARGIN + i * SIDE
                y1 = HEIGHT - MARGIN
                self.canvas.create_line(x0, y0, x1, y1, fill=color)

                x0 = MARGIN
                y0 = MARGIN + i * SIDE
                x1 = WIDTH - MARGIN
                y1 = MARGIN + i * SIDE
                self.canvas.create_line(x0, y0, x1, y1, fill=color)

        def __draw_puzzle(self):
            self.canvas.delete("numbers")
            for i in xrange(9):
                for j in xrange(9):
                    answer = self.game.puzzle[i][j]
                    if answer != 0:
                        x = MARGIN + j * SIDE + SIDE / 2
                        y = MARGIN + i * SIDE + SIDE / 2
                        original = self.game.start_puzzle[i][j]
                        color = "black" if answer == original else "sea green"
                        self.canvas.create_text(x, y, text=answer, tags="number", fill=color)

        def __clear_answers(self):
            self.game.start()
            self.canvas.delete("victory")
            self.__draw_puzze()

        def __cell_clicked(self, event):  # event has x, y coords of mouse click
            if self.game.game_over:
                return

            x, y = event.x, event.y
            if (MARGIN < x < WIDTH - MARGIN) and (MARGIN < Y < HEIGHT - MARGIN):
                self.canvas.focus_set()

                # get row and col numbers from x, y coords
                row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

                # if cell already selected then deselect it
                if (row, col) == (self.row, self.col):
                    self.row, self.col = -1, -1  # outside the grid
                elif self.game.puzzle[row][col] == 0:
                    self.row, self.col = row, col

            self.__draw_cursor()

        def __draw_cursor(self):
            self.canvas.delete("cursor")
            if self.row >= 0 and self.col >= 0:
                x0 = MARGIN + self.col * SIDE + 1
                y0 = MARGIN + self.row * SIDE + 1
                x1 = MARGIN + (self.col + 1) * SIDE - 1
                y1 = MARGIN + (self.row + 1) * SIDE - 1
                self.canvas.create_rectangle(
                    x0, y0, x1, y1,
                    outline ="red", tags ="cursor"
                )


if __name__ == '__main__':
    frame = SudokuUI()
