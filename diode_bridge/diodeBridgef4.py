import schemdraw
import schemdraw.elements as elm

# Create a new schematic diagram object
with schemdraw.Drawing() as d:

    # add the rectifier component
    d += (D := elm.Rectifier())

    # add label in the correct position
    d += elm.Label().label(" Ac ~ ").at(D.N)
    d += elm.Label().label(" Ac ~ ",loc='bottom').at(D.S)
    d += elm.Label().label(" Dc - ",loc="left").at(D.W)
    d += elm.Label().label(" Dc + ",loc="right").at(D.E)

    d.draw()