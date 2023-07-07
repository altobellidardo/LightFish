import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    # Get the default size of the drawing elements
    unit = d.unit

    d += elm.Diode()