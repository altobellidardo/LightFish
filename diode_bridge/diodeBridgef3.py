import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:

    d += elm.Diode().theta(45).dot()
    d += elm.Diode().theta(-45).dot()
    d += elm.Diode().theta(-135).dot()
    d += elm.Diode().theta(-225).dot()

    d.draw()