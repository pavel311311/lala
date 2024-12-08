import gdsfactory as gf
from .pad import pad_solder

'''
The PD Pad Layout below
    ------------
    ---p1---p4--
    ---p2-------      
    ---p3---p5--
    ------------
pad_size =(p1, p2, p3, p4, p5)
'''
pad_size = ((139.5, 77), (139.5,65), (139.5,77), (148.5,71), (148.5,71))
solder_size = ((23.985,40), (23.985,40), (23.985,40), (77.213,40), (77.213,40)) 
pad_position1 = ((0,0), (0,-131.25), (0,-262.5), (222.5, 3.75), (222.5, -256.25))
pad_position2 = ((0,0), (0,-131.25), (0,-262.5), (222.5, -6.25), (222.5, -256.25))
pad_position3 = ((0,0), (0,-131.25), (0,-262.5), (222.5, -6.25), (222.5, -266.25))
pitch = 500

@gf.cell
def pd_single(pad_size, solder_size, pad_position) -> gf.Component:
    '''
    ------------
    ---p1---p4--
    ---p2-------      
    ---p3---p5--
    ------------
    '''
    c = gf.Component()
    for n in range(5):
        c.add_ref(gf.components.pad(size=pad_size[n])).move(pad_position[n])
        c.add_ref(pad_solder(size=solder_size[n])).move(pad_position[n])
    return c

@gf.cell
def pd_array() -> gf.Component:
    c = gf.Component()
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position1))
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-1)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-2)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-3)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-4)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-5)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position2)).movey(pitch*-6)
    c.add_ref(pd_single(pad_size=pad_size, solder_size=solder_size, pad_position=pad_position3)).movey(pitch*-7)
    return c




