import schemdraw
import schemdraw.elements as elm

# Create a new schematic diagram object
with schemdraw.Drawing() as d:
    
    # create 4 diodes
    for i in range(4):
        # in the 3 and 4 time the diode are reversed
        if (i>1): d += elm.Diode().theta(45-90*i).dot().reverse()
        else: d += elm.Diode().theta(45-90*i).dot()
        
        # put the tag in all the diodes
        if (i == 0): d += elm.Label().label(" Ac ~ ")
        if (i == 1): d += elm.Label().label(" Dc + ",loc="right")
        if (i == 2): d += elm.Label().label(" Ac ~ ")
        if (i == 3): d += elm.Label().label(" Dc - ",loc="left")
        
    d.draw()