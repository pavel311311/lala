import gdsfactory as gf

def outline(size=(1500,4500),w=50) -> gf.Component:
    """
    the outline define
    """
    c =  gf.Component()
    c1 = c << gf.components.rectangle(size=size)
    c2 = c << gf.components.rectangle(size=(size[0]-w*2,size[1]-w*2))
    c2.movex(w)
    c2.movey(w)
    cc = gf.boolean(A=c1, B=c2, operation='not')
    return cc