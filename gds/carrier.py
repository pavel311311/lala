import gdsfactory as gf
c = gf.Component()

#create polygon outline
p1 = gf.kdb.DPolygon([(0,0),(1600,0),(1600,1980),(0,1980)])
r1 = gf.kdb.Region(p1.to_itype(gf.kcl.dbu))  # convert from um to DBU
r2 = r1.sized(-30000)
r3 = r1 -r2
c.add_polygon(r3,layer=(2,0))

#create concentric_circle model
def create_concentric_circles(radii=[30, 20], position=[150,150],layer=(1, 0)):
    c = gf.Component()
    c2 = gf.Component()        
    e1 = c << gf.components.circle(radii[0], layer=layer)
    e2 = c << gf.components.circle(radii[1], layer=layer)
    circle_con = c2  << gf.boolean(A=e1, B=e2, operation="not", layer=layer)
    circle_con.dmove(position)
    return c2

#create mark1,mark2
c << create_concentric_circles([60,30],position=[150,1980-150],layer=(1,0))
c << create_concentric_circles([60,30],position=[1600-150,1980-150],layer=(1,0))

# create polgyon
c.add_polygon([(320,52),(320+430,52),(320+430,52+860),(320+430-250,52+860),(320+430-250,52+860+520),
               (320+430-250+140,52+860+520),(320+430-250+140,52+860+520+400),
               (320+430-250+140-300,52+860+520+400)],layer=(2,0))

dot2 = (624,981)
c.add_polygon([dot2,(dot2[0]+200,dot2[1]),
               (dot2[0]+200,dot2[1]+920),
               (dot2[0],dot2[1]+920)],layer=(2,0))


#c.write_gds("interposer.gds")
c.show()