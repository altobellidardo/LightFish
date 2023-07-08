import schemdraw
import schemdraw.elements as elm

ic4033 = {
    # CD4033 - CMOS decade counter w/ 7-segment output - IC Element
    'h': 3,
    'label': 'CD4033',
    'pins': [
           elm.IcPin(name='CLK', pin='1', side='T', slot='10/10', rotation=90),
           elm.IcPin(name='INH', pin='2', side='T', slot='9/10', rotation=90),
           elm.IcPin(name='LT',  pin='14', side='T', slot='3/10', rotation=90),
           elm.IcPin(name='RBI', pin='3', side='T', slot='2/10', rotation=90),
           elm.IcPin(name='RST', pin='15', side='T', slot='1/10', rotation=90),
           elm.IcPin(name='A',  pin='10', side='B', slot='10/10', rotation=90),
           elm.IcPin(name='B',  pin='12', side='B', slot='9/10', rotation=90),
           elm.IcPin(name='C',  pin='13', side='B', slot='8/10', rotation=90),
           elm.IcPin(name='D',  pin='9', side='B', slot='7/10', rotation=90),
           elm.IcPin(name='E',  pin='11', side='B', slot='6/10', rotation=90),
           elm.IcPin(name='F',  pin='6', side='B', slot='5/10', rotation=90),
           elm.IcPin(name='G',  pin='7', side='B', slot='4/10', rotation=90),
           elm.IcPin(name='CO',  pin='5', side='B', slot='2/10', rotation=90),
           elm.IcPin(name='RBO',  pin='4', side='B', slot='1/10', rotation=90)]}

with schemdraw.Drawing() as d:
    d += (ic1 := elm.Ic(**ic4033))
    d.move_from(ic1.pin1, dx=4)
    d += (ic2 := elm.Ic(**ic4033).anchor('pin15'))
    d.move_from(ic2.pin1, dx=4)
    d += (ic3 := elm.Ic(**ic4033).anchor('pin15'))
    
    d.move_from(ic1.pin10, dx=.5, dy=-3)
    d += (seg1 := elm.SevenSegment(digit=0, cathode=True).right().anchor('a'))
    d += elm.Ground(lead=False).at(seg1.cathode)
    d += elm.RightLines(n=7).at(seg1.a).to(ic1.pin10)
    d.move_from(ic2.pin10, dx=.5, dy=-3)
    d += (seg2 := elm.SevenSegment(digit=1, cathode=True).right().anchor('a'))
    d += elm.Ground(lead=False).at(seg2.cathode)
    d += elm.RightLines(n=7).at(seg2.a).to(ic2.pin10)
    d.move_from(ic3.pin10, dx=.5, dy=-3)
    d += (seg3 := elm.SevenSegment(digit=2, cathode=True).right().anchor('a'))
    d += elm.Ground(lead=False).at(seg3.cathode)
    d += elm.RightLines(n=7).at(seg3.a).to(ic3.pin10)
    
    d += elm.Line().at(ic2.pin5).down(.5)
    d += elm.Wire('c', k=-2).to(ic1.pin1)
    d += elm.Line().at(ic3.pin5).down(.5)
    d += elm.Wire('c', k=-2).to(ic2.pin1)
    
    for ic in [ic1, ic2, ic3]:
        d += elm.Vdd().at(ic.RBI).label('+5V')
        d += elm.Wire('n').at(ic.pin14).to(ic.pin2)
        d += elm.Line().at(ic.pin2, dy=1).right(.5).idot()
        d += elm.Ground()

    d += elm.Line().at(ic3.pin1).right(2)
    d += (sw1 := elm.Button().label('Increment'))
    d += elm.Resistor().down().label('10K')
    d += elm.Ground()
    
    d += elm.Line().up(2).at(ic1.pin15)
    d += elm.Line().tox(ic2.pin15).dot()
    d += elm.Line().toy(ic2.pin15).hold()
    d += elm.Line().tox(ic3.pin15).dot()
    d += elm.Line().toy(ic3.pin15).hold()
    d += elm.Line().tox(sw1.start)
    d += elm.Button().label('Reset')
    d += elm.Wire('-|').delta(1.5, -2)
    d += elm.Resistor().down().label('10K', 'bottom')
    d += elm.Ground()

    d.move(dx=-4, dy=-1)
    d += elm.Label().label('Note CD4033:\npin 16 Vcc\npin8 ground')

    d.draw()