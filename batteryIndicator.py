import schemdraw
import schemdraw.elements as elm

# Battery Indicator

d = schemdraw.Drawing()

d += elm.Ground()
d += elm.Line().dot()
d += (r3 := elm.Resistor().up().label('3.3KΩ', 'bottom').dot())
d += (r2 := elm.Resistor().label('47KΩ', 'bottom').dot())
d += elm.Line().at(r2.istart, dy=-.4).left(d.unit/2).idot()
d += elm.Resistor().toy(r2.iend.y+.4).label('10KΩ')
d += elm.Line().tox(r2.iend).dot()
d += elm.Line().at(r2.end).up(d.unit/4)
d += elm.Vdd().label('Vcc')

d += elm.Line().right(d.unit/2).at(r3.end)
d += (Q := elm.BjtNpn2().up(2).anchor('base'))
d += elm.Line().at(Q.collector).right(d.unit/3)
d += elm.LED().toy(Q.emitter).dot().idot().label('Red').fill('red')
d += elm.Line().tox(Q.emitter).hold()
d += elm.LED().toy(r3.start).label('Green').fill('green')
d += elm.Line().tox(r3.start)
d += elm.Resistor().at(Q.collector, dx=d.unit/3).toy(r2.end).label('470Ω', 'bottom')
d += elm.Line().tox(r2.end)
    
d.draw()