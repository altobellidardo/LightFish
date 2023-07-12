import schemdraw
import schemdraw.elements as elm

# Create a new schematic diagram object
with schemdraw.Drawing() as d:

    # add didoes in 90 grades of difference
    d += elm.Diode().theta(45).dot()
    d += elm.Diode().theta(-45).dot()
    d += elm.Diode().theta(-135).dot()
    d += elm.Diode().theta(-225).dot()

    d.draw()