import schemdraw
import schemdraw.elements as elm

# Pull Up Circuit

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Add the tag for the output pin
    d += elm.Tag().label('Out')

    # Add a wire to the left net
    d += elm.Line(d.unit*.5).left()

    # Save the position of the net
    d.push()

    # Add the switch that makes the connection
    d += elm.Switch().down()

    # Add the ground connection
    d += elm.Ground()

    # Return to the saved position of the net
    d.pop()

    # Add the pull-up resistor
    d += elm.Resistor().up().label('R1\n10k')

    # Add a tag to indicate the voltage of this point
    d += elm.Line().left().length(d.unit*.7).label('Vcc')

    # Add the DC source (battery)
    d += elm.BatteryCell().down().label('15v')

    d += elm.Line()
    d += elm.Ground()

    # Draw the schematic diagram
    d.draw()