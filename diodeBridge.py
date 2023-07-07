import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:

    for i in range(4):
        if (i>1): d += elm.Diode().theta(45-90*i).dot().reverse()
        else: d += elm.Diode().theta(45-90*i).dot()
        
        if (i == 0): d += elm.Label().label(" Ac ~ ")
        if (i == 1): d += elm.Label().label(" Dc + ",loc="right")
        if (i == 2): d += elm.Label().label(" Ac ~ ")
        if (i == 3): d += elm.Label().label(" Dc - ",loc="left")
        
    d.draw()