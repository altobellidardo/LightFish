# Import the necessary modules for creating the schematic diagram
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

    # Add the 9V voltage source and label it
    V1 = elm.SourceV().label('9v').length(unit*2)
    d += V1

    # Add the photoresistor
    Pr1 = elm.Photoresistor().down().dot().at((unit, unit*2))
    d += Pr1

    # Connect the voltage source to the photoresistor
    d += elm.Wire().at(V1.end).to(Pr1.start).dot()

    # Add the potentiometer
    P1 = elm.Potentiometer().dot().at(Pr1.end)
    d += P1

    # Connect the potentiometer to the voltage source
    d += elm.Wire().at(P1.end).to(V1.start)

    # Connect the potentiometer tap to itself
    d += elm.Wire('-|').at(P1.end).to(P1.tap)

    # Add the resistor and label it
    R1 = elm.Resistor().label('R1\n390', loc='bottom').down().length(unit*.5).at((unit*2, unit*2))
    d += R1

    # Add the LED and label it
    D1 = elm.LED().label('LED\n2v', loc='bottom').length(unit*.5).down()
    d += D1

    # Connect the photoresistor to the resistor
    d += elm.Wire().at(Pr1.start).to(R1.start)

    # Add the NPN transistor and label it
    Q1 = elm.BjtNpn().at(D1.end).anchor("collector").right().drop("base").label("Q1\nBC547")
    d += Q1

    # Connect the transistor emitter to the potentiometer
    d += elm.Wire('|-').at(Q1.emitter).to(P1.end)

    # Connect the transistor base to the photoresistor
    d += elm.Wire('|-').at(Q1.base).to(Pr1.end)

    # Draw the schematic diagram
    d.draw()
