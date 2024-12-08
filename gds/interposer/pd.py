import gdsfactory as gf
import pad

@gf.cell
def pd_single_gcs_1() -> gf.Component:
    '''
    ------------
    ---p1---p4--
    ---p2-------      
    ---p3---p5--
    ------------
    '''
    c = gf.Component()

    p1_size = (139.5,77)
    p2_size = (139.5,65)
    p3_size = p1_size
    p4_size = (148.5,71)
    p5_size = p4_size

    p1_solder = (23.985,40)
    p2_solder =(23.985,40)
    p3_solder = p1_solder
    p4_solder = (77.213,40)
    p5_solder = (77.213,40)

    p1 = (0,0)
    p2 = (0, -131.25)
    p3 = (0, -262.5)
    p4 = (222.5, 3.75)
    p5 = (222.5, -256.25)

    c_p1 = c.add_ref(gf.components.pad(size=p1_size))
    c_p2 = c.add_ref(gf.components.pad(size=p2_size))
    c_p2.move(p2)
    c_p3 = c << gf.components.pad(size=p3_size)
    c_p3.move(p3)
    c_p4 = c << gf.components.pad(size=p4_size)
    c_p4.move(p4)
    c_p5 = c << gf.components.pad(size=p5_size)
    c_p5.move(p5)

    c_solder1 = c << pad.pad_solder(size=p1_solder)
    c_solder2 = c << pad.pad_solder(size=p2_solder)
    c_solder2.move(p2)
    c_solder3 = c << pad.pad_solder(size=p3_solder)
    c_solder3.move(p3)
    c_solder4 = c << pad.pad_solder(size=p4_solder)
    c_solder4.move(p4)
    c_solder5 = c << pad.pad_solder(size=p5_solder)
    c_solder5.move(p5)
    return c

@gf.cell
def pd_single_gcs_2() -> gf.Component:
    '''
    ------------
    ---p1---p4--
    ---p2-------      
    ---p3---p5--
    ------------
    '''
    c = gf.Component()

    p1_size = (139.5,77)
    p2_size = (139.5,65)
    p3_size = p1_size
    p4_size = (148.5,71)
    p5_size = p4_size

    p1_solder = (23.985,40)
    p2_solder =(23.985,40)
    p3_solder = p1_solder
    p4_solder = (77.213,40)
    p5_solder = (77.213,40)

    p1 = (0,0)
    p2 = (0, -131.25)
    p3 = (0, -262.5)
    p4 = (222.5, -6.25)
    p5 = (222.5, -256.25)

    c_p1 = c << gf.components.pad(size=p1_size)
    c_p2 = c << gf.components.pad(size=p2_size)
    c_p2.move(p2)
    c_p3 = c << gf.components.pad(size=p3_size)
    c_p3.move(p3)
    c_p4 = c << gf.components.pad(size=p4_size)
    c_p4.move(p4)
    c_p5 = c << gf.components.pad(size=p5_size)
    c_p5.move(p5)

    c_solder1 = c << pad.pad_solder(size=p1_solder)
    c_solder2 = c << pad.pad_solder(size=p2_solder)
    c_solder2.move(p2)
    c_solder3 = c << pad.pad_solder(size=p3_solder)
    c_solder3.move(p3)
    c_solder4 = c << pad.pad_solder(size=p4_solder)
    c_solder4.move(p4)
    c_solder5 = c << pad.pad_solder(size=p5_solder)
    c_solder5.move(p5)
    return c
##

@gf.cell
def pd_array_gcs() -> gf.Component:
    c = gf.Component()
    c.add_ref(pd_single_gcs_1())
    c.add_ref(pd_single_gcs_2()).movey(-500)
    c.add_ref(pd_single_gcs_2()).movey(-500*2)
    c.add_ref(pd_single_gcs_2()).movey(-500*3)
    c.add_ref(pd_single_gcs_2()).movey(-500*4)
    c.add_ref(pd_single_gcs_2()).movey(-500*5)
    c.add_ref(pd_single_gcs_2()).movey(-500*6)
    c.add_ref(pd_single_gcs_1()).movey(-500*7)
    return c




