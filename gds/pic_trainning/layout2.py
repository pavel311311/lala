import gdsfactory as gf
c = gf.Component()


c2 = gf.Component()
c2.add_polygon([(0,0),(2,0),(2,2),(0,2)],layer=(1,0))

c3 = gf.components.text("abc",position=(3,3),size=0.5)

p1 =gf.kdb.DPolygon([(0,0),(2.5,0),(2.5,2.5),(0,2.5)])
pp1 = gf.kdb.Region(p1.to_itype(gf.kcl.dbu))  # convert from um to DBU
pp2 = pp1.sized(10)
c4 = pp2 -pp1


c_p2 = c.add_polygon(c4, layer=(2,0))

c_p1 = c << c2
c_t1 = c << c3

c.write_gds("demo.gds")
c.show()