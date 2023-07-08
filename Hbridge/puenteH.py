import schemdraw
import schemdraw.elements as elm

""" 
H Bridge

This circuit is used to control the direction and speed of a DC motor or
a stepper motor. It allows current to flow in both directions through the motor,
enabling it to rotate in both directions.
"""

# Create a new schematic diagram object
with schemdraw.Drawing() as d:

    # Get the default size of the drawing elements
    unit = d.unit

    # Add the Vcc tag
    d += elm.Vdd().label("Vcc")

    # Add the 5V voltage source
    d += elm.SourceV().down(unit*2).reverse().label("5v", loc="bottom")

    # Add the ground connection
    d += elm.Ground()

    # Add components and label them
    d += (Vcc := elm.Vdd().label("Vcc").at((unit*2.3, 0)))
    d += (Q1 := elm.BjtPnp().left().anchor("collector").reverse().flip().at((unit*1.5, -.5*unit)).label("Q1"))
    d += (Q2 := elm.BjtNpn().left().anchor("collector").reverse().flip().at((unit*1.5, unit*-1.5)).label("Q2"))
    d += (Q3 := elm.BjtPnp().left().anchor("collector").flip().at((unit *3, -.5*unit)).label("Q3", loc="left"))
    d += (Q4 := elm.BjtNpn().left().anchor("collector").flip().at((unit *3, unit*-1.5)).label("Q4", loc="left"))
    d += (M1 := elm.Motor().at((unit*2.75, -unit)).label("Motor"))
    d += (Gnd1 := elm.Ground().at((unit*2.3, unit*-2)))
    d += (InA := elm.Tag().label("InA").at((Q3.base[0]+unit*.5, Q3.base[1])).reverse())
    d += (InB := elm.Tag().label("InB").at((Q4.base[0]+unit*.5, Q4.base[1])).reverse())
    d += (InC := elm.Tag().label("InC").at(Q1.base))
    d += (InD := elm.Tag().label("InD").at(Q2.base))

    # Connect the components with wires
    d += elm.Wire('|-').at(Q1.emitter).to(Vcc.end)
    d += elm.Wire('-|').at(Vcc.end).to(Q3.emitter)
    d += elm.Wire('|-').at(Q1.collector).to(M1.end)
    d += elm.Wire('-|').at(M1.end).to(Q2.collector)
    d += elm.Wire('|-').at(Q2.emitter).to(Gnd1.start)
    d += elm.Wire('-|').at(Gnd1.start).to(Q4.emitter)
    d += elm.Wire('|-').at(Q4.collector).to(M1.start)
    d += elm.Wire('-|').at(M1.start).to(Q3.collector)

    # Draw the schematic diagram
    d.draw()
