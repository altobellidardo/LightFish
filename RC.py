import schemdraw
import schemdraw.elements as elm

# RC circuit

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Add the tag for the output pin
    d += elm.Tag().label('Out')

    # Add a wire to the left net
    d += elm.Line().left()

    # Save the position of the net
    d.push()

    # Add the capacitor
    d += elm.Capacitor().down().label('C1\n10uF')

    # Add the ground connection
    d += elm.Ground()

    # Return to the saved position of the net
    d.pop()

    # Add the resistor
    d += elm.Resistor().up().label('R1\n10k')

    # Add a tag to indicate the voltage of this point
    d += elm.Line().left().length(d.unit*.7).label('Vcc')

    # Add the DC source (battery)
    d += elm.BatteryCell().down().label('15v', loc='bottom')

    d += elm.Line()
    d += elm.Ground()

    # Draw the schematic diagram
    d.draw()