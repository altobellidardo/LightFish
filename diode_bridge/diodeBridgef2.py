import schemdraw
import schemdraw.elements as elm

# Create a new schematic diagram object
with schemdraw.Drawing() as d:

    # configure another font
    d.config(font="serif")

    # add the rectifier commponent
    d += (D := elm.Rectifier())

    # The input labels
    d += elm.Line().left(d.unit*1.5).at(D.N).dot(open=True).idot()
    d += elm.Line().left(d.unit*1.5).at(D.S).dot(open=True).idot()
    d += elm.Gap().toy(D.N).label(['~', 'AC IN', '~'])

    # The output label
    d += elm.Line().at(D.E).right(d.unit*.8).dot(open=True).idot()
    d += elm.Line().down(d.unit*1).at(D.W)
    d += elm.Line().right(d.unit*2.25).dot(open=True).idot()
    d += elm.Gap().toy(D.E).label(['-', 'DC OUT', '+'])

    d.draw()