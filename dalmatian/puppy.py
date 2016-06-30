import random


class Puppy(object):

    def __init__(self):
        self.spots = []
        n_spots = random.randint(1, 10)
        for i in range(n_spots):
            spot = {'x': random.randint(0, 100),
                    'y': random.randint(0, 100),
                    'r': random.randint(1, 10),
                    }
            self.spots.append(spot)

    def __repr__(self):
        return str(self.spots)

    def write_svg(self, filename):
        xml_header = """<?xml version="1.0"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <rect widht="100" height="100" fill="white" />
"""
        svg_file = open(filename, 'w')
        svg_file.write(xml_header)
        for spot in self.spots:
            svg_file.write('  <circle cx="{}" cy="{}" r="{}" fill="black"'
                           '/>\n'.format(spot['x'], spot['y'], spot['r']))
        svg_file.write('</svg>\n')
        svg_file.close()
