import gdsfactory as gf

# Create a blank component (essentially an empty GDS cell with some special features)
c = gf.Component()
p1 = c.add_polygon([(-8, -6), (6, 10), (7, 17), (9, 5)], layer=(1, 0))
c.write_gds("demo.gds")  # write it to a GDS file. You can open it in klayout.
c.show()  # show it in klayout