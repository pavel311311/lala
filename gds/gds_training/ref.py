import gdsfactory as gf
import matplotlib.pyplot as plt

# create component
p = gf.Component()

# add a polygon
xpts = [0, 0, 5, 6, 9, 12]
ypts = [0, 1, 1, 2, 2, 0]
xypts = list(zip(xpts, ypts))
p.add_polygon(xypts, layer=(1,0))

#create c
c = gf.Component()
poly_ref1 = c << p
poly_ref2 = c << p
poly_ref3 = c << p

poly_ref2.drotate(90)
poly_ref3.drotate(180)

#change p
xpts = [14, 14, 16, 16]
ypts = [0, 2, 2, 0]
xypts = list(zip(xpts, ypts))
p.add_polygon(xypts, layer=(2,0))

#create another c2, to add ref c
c2 =  gf.Component()
d_ref1 = c2.add_ref(c)
d_ref2 = c2 << c
d_ref3 = c2 << c

d_ref1.move([20,0])
d_ref2.move([40,0])

c2.plot()
plt.show()

