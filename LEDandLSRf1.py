import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:

    unit = d.unit

    V1 = d.add(elm.SourceV().label('9v').length(unit*2))
    d.add(elm.Line().right(unit*.75).dot())
    L1 = d.add(elm.Photoresistor().down().dot())
    P1 = d.add(elm.Potentiometer().dot())
    d.add(elm.Line().right(unit*.25))
    d.add(elm.Line().up(unit*.5))
    d.add(elm.Line().left(d.unit*.75).at(P1.end))
    d.add(elm.Line().at(L1.start).right())
    d.add(elm.Resistor().label('R1\n390',loc='bottom').down().length(unit*.5))
    D1 = d.add(elm.LED().label('LED\n2v',loc='bottom').length(unit*.5))
    Q1 = d.add(elm.BjtNpn().at(D1.end).anchor("collector").right().drop("base").label("Q1\nBC547"))
    d.add(elm.Line().left(unit*.5))
    d.add(elm.Line().up(unit*.225))
    d.add(elm.Line().left(unit*.25))
    d.add(elm.Line().at(Q1.emitter).down(unit*.535))
    d.add(elm.Line().left(unit*.75))

    d.draw()