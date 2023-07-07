# Import the necessary modules for creating the schematic diagram
import schemdraw
import schemdraw.elements as elm

# circuit of charge or discharge the capacitor depending on the switch position.

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    # Add the 5V voltage source and label it
    V1 = elm.SourceV().label('5V')
    d += V1

    # Add a horizontal line
    d += elm.Line().right(d.unit*.75)

    # Add the SPDT switch, label it, and set its initial state
    S1 = elm.SwitchSpdt2(action='close').up().anchor('b').label('$t=0$', loc='rgt')
    d += S1

    # Add another horizontal line starting from the center of the switch
    d += elm.Line().right(d.unit*.75).at(S1.c)

    # Add the resistor and label it
    d += elm.Resistor().down().label('$100\Omega$').label(['+','$v_o$','-'], loc='bot')

    # Connect the components with lines
    d += elm.Line().to(V1.start)  # Connect the line to the voltage source
    d += elm.Capacitor().at(S1.a).toy(V1.start).label('1$\mu$F').dot()  # Connect the capacitor and label it
    d += elm.Ground()  # Add the ground connection

    # Draw the schematic diagram
    d.draw()
