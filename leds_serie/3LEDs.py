import schemdraw
import schemdraw.elements as elm

""" 
3 serial LEDs connected limited to 10mA

When multiple LEDs are connected in series, the current is the same for
all of them, and the sum of the voltage drops across each LED equals the
total applied voltage. This allows controlling multiple LEDs using a single
current or voltage source.
"""

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Get the default size of the drawing elements
    unit = d.unit

    # Add a voltage source element (9V) to the diagram
    d += (V1 := elm.SourceV().label('9v').length(unit*4))
    # Add the first LED element (D1) to the diagram
    d += (D1 := elm.LED().at((unit, unit*4)).down().label("D1\n2v"))
    # Add the second LED element (D2) to the diagram
    d += (D2 := elm.LED().label("D2\n2v"))
    # Add the third LED element (D3) to the diagram
    d += (D3 := elm.LED().label("D3\n2v"))
    # Add a resistor element (R1) to the diagram
    d += (R1 := elm.Resistor().label('R1\n300$\\Omega$', loc="bottom"))
    # Connect the voltage source to the first LED
    d += elm.Wire().at(V1.end).to(D1.start)
    # Connect the resistor to the voltage source
    d += elm.Wire().at(R1.end).to(V1.start)

    # Draw the schematic diagram
    d.draw()
