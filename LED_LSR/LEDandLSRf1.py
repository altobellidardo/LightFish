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
    V1 = d.add(elm.SourceV().label('9v').length(unit*2))
    d.add(elm.Line().right(unit*.75).dot())
    # add a photoresistor (LSR)
    L1 = d.add(elm.Photoresistor().down().dot())
    # add a potenciometer
    P1 = d.add(elm.Potentiometer().dot())
    d.add(elm.Line().right(unit*.25))
    d.add(elm.Line().up(unit*.5))
    d.add(elm.Line().left(d.unit*.75).at(P1.end))
    d.add(elm.Line().at(L1.start).right())
    d.add(elm.Resistor().label('R1\n390',loc='bottom').down().length(unit*.5))
    # add a LED 
    D1 = d.add(elm.LED().label('LED\n2v',loc='bottom').length(unit*.5))
    Q1 = d.add(elm.BjtNpn().at(D1.end).anchor("collector").right().drop("base").label("Q1\nBC547"))
    d.add(elm.Line().left(unit*.5))
    d.add(elm.Line().up(unit*.225))
    d.add(elm.Line().left(unit*.25))
    d.add(elm.Line().at(Q1.emitter).down(unit*.535))
    d.add(elm.Line().left(unit*.75))

    d.draw()