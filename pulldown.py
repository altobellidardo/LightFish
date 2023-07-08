import schemdraw
import schemdraw.elements as elm

""" 
Pull Down Circuit

Similar to pull-up, this circuit is used to ensure that an input pin has a
low logic state when no external signal is applied. It consists of a resistor
connected between the input pin and a negative voltage source or ground (GND).
"""

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Add the tag for the output pin
    d += elm.Tag().label('Out')

    # Add a wire to the left net
    d += elm.Line().left()

    # Save the position of the net
    d.push()

    # Add the pull-down resistor
    d += elm.Resistor().down().label('R1\n10k')

    # Add the ground connection
    d += elm.Ground()

    # Return to the saved position of the net
    d.pop()

    # Add the switch that closes the circuit and changes the output to Vcc
    d += elm.Switch().up()

    # Add a tag to indicate the voltage of this point
    d += elm.Line().left().length(d.unit*.7).label('Vcc')

    # Add the DC source (battery)
    d += elm.BatteryCell().down().label('15v', loc='bottom')

    d += elm.Line()
    d += elm.Ground()

    # Draw the schematic diagram
    d.draw()