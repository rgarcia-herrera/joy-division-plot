import svgwrite
from svgwrite import cm, mm   



class JoyDivisionPlot:

    def __init__(self, grid, filename='joy_division_plot.svg'):
        self.dwg  = svgwrite.Drawing(filename=filename, debug=True)
        self.grid = grid

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
