import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:

    d.config(font="serif")

    d += (D := elm.Rectifier())

    d += elm.Line().left(d.unit*1.5).at(D.N).dot(open=True).idot()
    d += elm.Line().left(d.unit*1.5).at(D.S).dot(open=True).idot()
    d += elm.Gap().toy(D.N).label(['~', 'AC IN', '~'])

    d += elm.Line().at(D.E).right(d.unit*.8).dot(open=True).idot()
    d += elm.Line().down(d.unit*1).at(D.W)
    d += elm.Line().right(d.unit*2.25).dot(open=True).idot()
    d += elm.Gap().toy(D.E).label(['-', 'DC OUT', '+'])

    d.draw()