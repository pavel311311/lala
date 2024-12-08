import gdsfactory as gf

c = gf.Component()

c.add_polygon(points=[(0,0),(4,0),(4,4),(0,4)]
               ,layer=(1,0))

p2 = gf.components.regular_polygon()
c.write_gds("test.gds")
c.show()
