import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:

    d += (D := elm.Rectifier())

    d += elm.Label().label(" Ac ~ ").at(D.N)
    d += elm.Label().label(" Ac ~ ",loc='bottom').at(D.S)
    d += elm.Label().label(" Dc - ",loc="left").at(D.W)
    d += elm.Label().label(" Dc + ",loc="right").at(D.E)

    d.draw()