from globalValues import *


def prepareMap():
    matrix = []
    for _ in range(HEIGHT):
        row = []
        for _ in range(WIDTH):
            row.append(False)
        matrix.append(row)
    return matrix