from pprint import pprint
import csv
import random

from jdp import JoyDivisionPlot
    





grid = []
for l in range(100):
    grid.append( [random.randrange(-2,2) for d in range(1,50)] )


p = JoyDivisionPlot(grid)    
p.piled_lineplots()
p.dwg.save()
