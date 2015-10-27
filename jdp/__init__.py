import svgwrite
from svgwrite import cm, mm   
import numpy as np
from pprint import pprint

class JoyDivisionPlot:

    def __init__(self, grid, filename='joy_division_plot.svg'):
        self.dwg  = svgwrite.Drawing(filename=filename, debug=True)
        self.grid = np.array(grid)

    def piled_lineplots(self, stroke='gray', fill="none", stroke_width="0.5", stroke_opacity="0.2", **kwargs):
        hlines = self.dwg.add(self.dwg.g(id='hlines',
                                         stroke=stroke,
                                         fill=fill,
                                         stroke_width=stroke_width,
                                         stroke_opacity=stroke_opacity,
                                         **kwargs))
        y = 1
        for line in self.grid:
            points = []
            x = 1
            for column in line:
                points.append( (x, (y-column)) )
                x+=3
            hlines.add(self.dwg.polyline(points))
            y+=1


    def side_plot(self, stroke='gray', fill="none", stroke_width="0.5", stroke_opacity="0.5", **kwargs):
        sideplot = self.dwg.add(self.dwg.g(id='side',
                                           stroke=stroke,
                                           fill=fill,
                                           stroke_width=stroke_width,
                                           stroke_opacity=stroke_opacity,
                                           **kwargs))

        x = len(self.grid[0])*3
        y = 1
        points = []        
        for line in self.grid:
            print line
            print line.max()
            points.append( (x+line.max(), y) )
            y+=1

        pprint(points)
        sideplot.add(self.dwg.polyline(points))

