import schemdraw
import schemdraw.elements as elm

""" 
Circuit to change the intensity of the light with the brightness

An LDR is used to adjust the brightness of an LED based on the ambient
light intensity. As the incident light on the LDR varies, its resistance changes,
affecting the current flowing through the LED, and thus its brightness.
"""

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Get the default size of the drawing elements
    unit = d.unit

    # add a 9v battery
    d += (V1 := elm.SourceV().label('9v').length(unit*2))
    d += elm.Line().right(unit*.75).dot()
    # add a photoresistor and potenciometer in serie
    d += (L1 := elm.Photoresistor().down().dot())
    d += (P1 := elm.Potentiometer().dot())
    d += elm.Line().right(unit*.25)
    d += elm.Line().up(unit*.5)
    d += elm.Line().left(d.unit*.75).at(P1.end)
    d += elm.Line().at(L1.start).right()
    d += elm.Resistor().label('R1\n390', loc='bottom').down().length(unit*.5)
    d += (D1 := elm.LED().label('LED\n2v', loc='bottom').length(unit*.5))
    d += (Q1 := elm.BjtNpn().at(D1.end).anchor("collector").right().drop("base").label("Q1\nBC547"))
    d += elm.Line().left(unit*.5)
    d += elm.Line().up(unit*.225)
    d += elm.Line().left(unit*.25)
    d += elm.Line().at(Q1.emitter).down(unit*.535)
    d += elm.Line().left(unit*.75)

    d.draw()
