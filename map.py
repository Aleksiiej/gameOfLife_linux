from globalValues import *
from cell import Cell

def prepareMap(cellGroup):
    x = 0
    y = 0
    for _ in range(HEIGHT):
        for _ in range(WIDTH):
            cellGroup.add(
                Cell(
                    CELL_SIZE - 2,
                    CELL_SIZE - 2,
                    CELL_SIZE / 2 + x * CELL_SIZE,
                    CELL_SIZE / 2 + y * CELL_SIZE,
                    BLUE
                )
            )
            x += 1
        x = 0
        y += 1