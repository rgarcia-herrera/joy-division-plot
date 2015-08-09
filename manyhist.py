from pprint import pprint
import svgwrite
from svgwrite import cm, mm   
import csv
import random

def piled_lineplot(drwng, grid):

    hlines = drwng.add(drwng.g(id='hlines', stroke='gray', fill="none", stroke_width="0.5", stroke_opacity="0.2"))

    y = 1
    for line in grid:
        points = []
        x = 1
        for column in line:
            points.append( (x, (y-column)) )
            x+=3
        hlines.add(drwng.polyline(points))
        y+=1


            

    

    
if __name__ == '__main__':
    dwg = svgwrite.Drawing(filename='aguas.svg', debug=True)
    rdr = csv.reader( open('histoai.csv','r') )
    grid = []
    for l in rdr:
        # grid.append( [int(d) for d in l] )
        grid.append( [random.randrange(-2,2) for d in range(1,100)] )

    piled_lineplot(dwg, grid)
    dwg.save()
