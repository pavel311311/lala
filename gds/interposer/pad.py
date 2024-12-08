import gdsfactory as gf

@gf.cell
def pad_solder(size=(100,80), layer=(1,0)) -> gf.Component:
    """
     椭圆形矩形PAD
    Args:
        length: 长度
    
    Returns:
        component
    """
    length = size[0]
    width = size[1]
    c =  gf.Component()

    rec = c << gf.components.rectangle(size=(length,width), layer=layer, centered=True)
    cir1 = c << gf.components.circle(radius=width/2, layer=layer)
    cir2 = c << gf.components.circle(radius=width/2, layer=layer)

    cir1.movex(-length/2)
    cir2.movex(length/2)

    pad_left = gf.boolean(A=rec,B=cir1,operation="or", layer=(1,0))
    pad = gf.boolean(A=pad_left, B=cir2,operation="or", layer=(1,0))

    return pad

#c = pad_solder()
#c.write_gds("solder_pad.gds")